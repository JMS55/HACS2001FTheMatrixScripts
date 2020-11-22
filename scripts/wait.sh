#!/bin/bash

container_id=$1
template_id=$2
container_ip=$3
mitm_port=$4
attacker_ip=$5

# Wait 10m for the attacker to do things
sleep 10m

# Remove firewall rule allowing attacker in, regardless of everyone else being blocked (set by monitor.sh)
iptables --table filter --delete INPUT --protocol tcp --source $attacker_ip --destination 172.20.0.1 --destination-port $mitm_port --jump ACCEPT

# DROP traffic from { $attacker_ip } to { containers } forever
iptables --table filter --insert INPUT 1 --source $attacker_ip --destination 172.20.0.1 --jump DROP

# Goto recyle.sh
/root/recycle.sh $container_id $template_id $container_ip $mitm_port &
