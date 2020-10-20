#!/bin/bash

container_id=$1
template_id=$2
mitm_port=$3
attacker_ip=$4

# Wait 15m for the attacker to do things
sleep 15m

# Remove firewall rules set by monitor.sh
iptables --table filter --delete INPUT --protocol tcp --source $attacker_ip --destination 172.20.0.1 --destination-port $mitm_port --jump ACCEPT
iptables --table filter --delete INPUT --protocol tcp --source 0.0.0.0/0 --destination 172.20.0.1 --destination-port $mitm_port --jump DROP

# DROP traffic from { $attacker_ip } to { containers } forever
iptables --table filter --insert INPUT 1 --source $attacker_ip --destination 172.20.0.1 --jump DROP

# Goto recyle.sh
/root/recycle.sh $container_id $template_id $mitm_port &
