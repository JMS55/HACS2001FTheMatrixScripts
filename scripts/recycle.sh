#!/bin/bash

container_id=$1
container_ip=""
template_id=$2
mitm_port=$3

if [[ $container_id == "101" ]]; then
    container_ip="172.0.0.2"
elif [[ $container_id == "102" ]]; then
    container_ip="172.0.0.3"
elif [[ $container_id == "103" ]]; then
    container_ip="172.0.0.4"
fi

if [[ $template_id == "202" ]]; then
    template_id="201"
else
    template_id="202"
fi

# Kill old MITM
pkill -xf "node /root/MITM/mitm/index.js HACS200_1F $mitm_port $container_ip $container_id true mitm_config.js"
pkill -xf "tail -n 0 -F /root/MITM_data/logins/${container_id}.txt"

# Destroy old container
pct unmount $container_id
pct stop $container_id --skiplock 1
pct unmount $container_id
pct destroy $container_id

# Create new container
pct unlock $template_id
while ! pct clone $template_id $container_id; do
    sleep 30;
done
pct unlock $template_id
pct set $container_id --net0 name=eth0,bridge=vmbr0,ip=${container_ip}/16,gw=172.20.0.1
pct start $container_id
pct unlock $container_id
rm -f /run/lock/lxc/pve-config-${container_id}.lock
pct mount $container_id

# Start MITM
node /root/MITM/mitm/index.js HACS200_1F $mitm_port $container_ip $container_id true mitm_config.js &
# Goto monitor.sh
tail -n 0 -F /root/MITM_data/logins/${container_id}.txt | /root/monitor.sh $container_id $template_id $mitm_port &
