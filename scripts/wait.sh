#!/bin/bash

container_id=$1
attacker_ip=$2

# Wait 15m for the attacker to do things
sleep 15m

# Remove firewall rules set by monitor.sh
iptables --table filter --delete INPUT --protocol tcp --source $attacker_ip --destination 172.20.0.1 --destination-port 10000 --jump ACCEPT
iptables --table filter --delete INPUT --protocol tcp --source 0.0.0.0/0 --destination 172.20.0.1 --destination-port 10000 --jump DROP

# DROP traffic from { $attacker_ip } to { container } forever
iptables --table filter --insert INPUT 1 --source $attacker_ip --destination 172.20.0.1 --jump DROP

# Goto recyle.sh
./recycle.sh $container_id &
