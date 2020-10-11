#!/bin/bash

container_id=$1
container_ip="172.20.0.2"
if [[ $container_id == "102" ]]; then
    container_ip="172.20.0.3"
fi

new_container_id=$container_id
new_container_ip=$container_ip
if [[ $new_container_id == "101" ]]; then
    new_container_id = "102"
    new_container_ip = "172.20.0.3"
else if [[ $new_container_id == "102" ]]; then
    new_container_id = "101"
    new_container_ip = "172.20.0.2"
fi

# Kill old MITM
pkill -xf "node /root/MITM/mitm/index.js HACS200_1F 10000 ${container_ip} ${container_id} true mitm_config.js"
pkill -xf "tail -n 0 -F /root/MITM_data/logins/${container_id}.txt"
# Destroy old container
pct unmount $container_id
pct stop $container_id --skiplock 1
pct unmount $container_id
pct destroy $container_id

# Create new container
pct create ${new_container_id} /var/lib/vz/template/cache/ubuntu-16.04-standard_16.04.5-1_amd64.tar.gz --storage local-lvm --net0 name=eth0,ip=${new_container_ip}/16,bridge=vmbr0,gw=172.20.0.1
pct start $new_container_id
# TODO: Add honey
# TODO: Add snoopy logger if needed
pct mount $new_container_id

# Start MITM
node /root/MITM/mitm/index.js HACS200_1F 10000 ${new_container_ip} ${new_container_id} true mitm_config.js &
# Goto monitor.sh
tail -n 0 -F /root/MITM_data/logins/${new_container_id}.txt | ./monitor.sh $new_container_id &
