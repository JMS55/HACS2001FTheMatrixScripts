#!/bin/bash

container_id=$1
template_id=$2
container_ip=$3
mitm_port=$4

# Remove firewall rule blocking anyone from interacting with the container (set by monitor.sh)
iptables --table filter --delete INPUT --protocol tcp --source 0.0.0.0/0 --destination 172.20.0.1 --destination-port $mitm_port --jump DROP

# Reads lines of MITM logs from STDIN
while read line; do
    attacker_ip=$(echo $line | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
    if [ ! -z "$attacker_ip" ]; then
        # ACCEPT traffic from { $attacker_ip } to { container }
        iptables --table filter --insert INPUT 1 --protocol tcp --source $attacker_ip --destination 172.20.0.1 --destination-port $mitm_port --jump ACCEPT
        # DROP traffic from { anywhere } to { container }
        iptables --table filter --insert INPUT 2 --protocol tcp --source 0.0.0.0/0 --destination 172.20.0.1 --destination-port $mitm_port --jump DROP

        # Goto wait.sh
        /root/wait.sh $container_id $template_id $container_ip $mitm_port $attacker_ip &
        break
    fi
done
