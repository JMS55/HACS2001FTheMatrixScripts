# HACS200 Group 1F - TheMatrix
## Scripts
#### monitor.sh
Monitors for attackers entering systems, and block form other entrace
#### recycle.sh
Recycles the container
#### wait.sh
Waits for time set, runs recycle.sh

## Honey

## Containers
#### Control
- pct create 101 /var/lib/vz/template/cache/ubuntu-16.04-standard_16.04.5-1_amd64.tar.gz --storage local-lvm --net0 name=eth0,ip=172.20.0.2/16,bridge=vmbr0,gw=172.20.0.1

- vzdump 101 --mode snapshot

#### Snoopy
- pct restore 102 /var/lib/vz/dump/vzdump-lxc-101-2020_10_04-17_46_07.tar --storage local-lvm --net0 name=eth0,ip=172.20.0.3/16,bridge=vmbr0,gw=172.20.0.1
- pct push 102 snoopy/ /snoopy

## Misc
#### Host VM login
To SSH into the HostVM: `ssh root@jump.aces.umd.edu -p15831`
Username: `root`
Password: `2fmatrix`
