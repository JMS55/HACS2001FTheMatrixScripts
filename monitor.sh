#!/bin/bash

container_id=$1

while read line; do
    attacker_ip=$(echo $line | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')

    echo "New login: $attacker_ip, $(date)" >> /root/${container_id}log

    iptables --table filter --insert INPUT 1 --protocol tcp --source $attacker_ip --destination 172.20.0.1 --destination-port 10000 --jump ACCEPT
    iptables --table filter --insert INPUT 2 --protocol tcp --source 0.0.0.0/0 --destination 172.20.0.1 --destination-port 10000 --jump DROP

    ./wait.sh $container_id $attacker_ip &
    exit
done
