#!/bin/bash

container_id=$1
container_ip="172.20.0.2"
if [[ $container_id == "102" ]]; then
    container_ip="172.20.0.3"
fi

pkill -xf "node /root/MITM/mitm/index.js HACS101_JMS 10000 ${container_ip} ${container_id} true mitm_${container_id}.js"
pkill -xf "tail -n 0 -F /root/MITM_data/logins/${container_id}.txt"
pct unmount $container_id
pct stop $container_id --skiplock 1
pct unmount $container_id
pct destroy $container_id

pct unlock 201
while ! pct clone 201 $container_id --experimental false; do
    sleep 30;
done
pct unlock 201
pct set $container_id --net0 name=eth0,bridge=vmbr0,ip=${container_ip}/16,gw=172.20.0.1
pct start $container_id
pct unlock $container_id
rm -f /run/lock/lxc/pve-config-${container_id}.lock
pct mount $container_id

echo "Recyled, $(date)" >> /root/${container_id}log

node /root/MITM/mitm/index.js HACS101_JMS 10000 ${container_ip} ${container_id} true mitm_${container_id}.js &
tail -n 0 -F /root/MITM_data/logins/${container_id}.txt | ./monitor.sh $container_id &
