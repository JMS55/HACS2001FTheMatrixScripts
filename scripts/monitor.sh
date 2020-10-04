#!/bin/bash

# Reads lines of MITM logs from STDIN
while read line; do
    attacker_ip=$(echo $line | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')

    # ACCEPT traffic from { $attacker_ip } to { container }
    iptables --table filter --insert INPUT 1 --protocol tcp --source $attacker_ip --destination 172.20.0.1 --destination-port 10000 --jump ACCEPT
    # DROP traffic from { anywhere } to { container }
    iptables --table filter --insert INPUT 2 --protocol tcp --source 0.0.0.0/0 --destination 172.20.0.1 --destination-port 10000 --jump DROP

    # Goto wait.sh
    ./wait.sh $attacker_ip &
    break
done
