#!/bin/bash

container_id=$1
template_id=$2
container_ip=$3
mitm_port=$4

if [[ $template_id == "202" ]]; then
    template_id="201"
else
    template_id="202"
fi

echo "Using template: ${template_id}"

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
    sleep 10;
done
pct unlock $template_id
pct set $container_id --net0 name=eth0,bridge=vmbr0,ip=${container_ip}/16,gw=172.20.0.1
pct start $container_id
pct unlock $container_id
rm -f /run/lock/lxc/pve-config-${container_id}.lock
pct mount $container_id

# Start MITM
sleep 1m
node /root/MITM/mitm/index.js HACS200_1F $mitm_port $container_ip $container_id true mitm_config.js &
sleep 1m
# Goto monitor.sh
tail -n 0 -F /root/MITM_data/logins/${container_id}.txt | /root/monitor.sh $container_id $template_id $container_ip $mitm_port &
