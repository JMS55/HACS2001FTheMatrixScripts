#!/bin/bash

container_id=$1
template_id=$2

# Reads lines of MITM logs from STDIN
while read line; do
    attacker_ip=$(echo $line | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')

    # ACCEPT traffic from { $attacker_ip } to { containers }
    iptables --table filter --insert INPUT 1 --protocol tcp --source $attacker_ip --destination 172.20.0.1 --destination-port 10000 --jump ACCEPT

    # Goto wait.sh
    /root/wait.sh $container_id $template_id $attacker_ip &
    break
done
