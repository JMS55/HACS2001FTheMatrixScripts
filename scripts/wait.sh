#!/bin/bash

container_id=$1
attacker_ip=$2

sleep 45m

iptables --table filter --delete INPUT --protocol tcp --source $attacker_ip --destination 172.20.0.1 --destination-port 10000 --jump ACCEPT
iptables --table filter --delete INPUT --protocol tcp --source 0.0.0.0/0 --destination 172.20.0.1 --destination-port 10000 --jump DROP

if [[ -f /var/lib/lxc/${container_id}/rootfs/root/malware.txt ]]; then
    iptables --table filter --insert INPUT 1 --source $attacker_ip --destination 172.20.0.1 --jump DROP
fi

./recycle.sh $container_id &
