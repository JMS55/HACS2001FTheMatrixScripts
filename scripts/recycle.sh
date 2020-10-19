#!/bin/bash

container_id=$1
container_ip="172.20.0.2"
new_container_id="102"
new_container_ip="172.20.0.3"
template_id="202"
if [[ $container_id == "102" ]]; then
    container_ip="172.20.0.3"
    new_container_id="101"
    new_container_ip="172.20.0.2"
    template_id="201"
fi

# Kill old MITM
pkill -xf "node /root/MITM/mitm/index.js HACS200_1F 10000 $container_ip $container_id true mitm_config.js"
pkill -xf "tail -n 0 -F /root/MITM_data/logins/${container_id}.txt"

# Destroy old container
pct unmount $container_id
pct stop $container_id --skiplock 1
pct unmount $container_id
pct destroy $container_id

# Create new container
pct unlock $template_id
while ! pct clone $template_id $new_container_id; do
    sleep 30;
done
pct unlock $template_id
pct set $new_container_id --net0 name=eth0,bridge=vmbr0,ip=${new_container_ip}/16,gw=172.20.0.1
pct start $new_container_id
pct unlock $new_container_id
rm -f /run/lock/lxc/pve-config-${new_container_id}.lock
pct mount $new_container_id

# Start MITM
node /root/MITM/mitm/index.js HACS200_1F 10000 $new_container_ip $new_container_id true mitm_config.js &
# Goto monitor.sh
tail -n 0 -F /root/MITM_data/logins/${new_container_id}.txt | /root/monitor.sh $new_container_id &
