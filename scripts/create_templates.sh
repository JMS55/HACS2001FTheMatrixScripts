pct unmount 101
pct destroy 101

pct unmount 102
pct destroy 102

pct unmount 103
pct destroy 103

pct destroy 201
pct create 201 /var/lib/vz/template/cache/ubuntu-16.04-standard_16.04.5-1_amd64.tar.gz --storage local-lvm --net0 name=eth0,ip=172.20.0.2/16,bridge=vmbr0,gw=172.20.0.1 -hostname backup
pct start 201
pct push 201 /root/honey.tar /root/honey.tar
pct push 201 /root/sshd_config /etc/ssh/sshd_config
pct exec 201 service ssh restart
pct exec 201 -- tar -xvf honey.tar
pct exec 201 -- rm honey.tar
pct exec 201 -- cp -r honey/. /home
pct exec 201 -- rm -rf honey

pct stop 201
pct template 201

pct destroy 202
pct create 202 /var/lib/vz/template/cache/ubuntu-16.04-standard_16.04.5-1_amd64.tar.gz --storage local-lvm --net0 name=eth0,ip=172.20.0.3/16,bridge=vmbr0,gw=172.20.0.1 -hostname backup
iptables --table nat --insert PREROUTING 1 --destination 172.30.133.255 --jump DNAT --to-destination 172.20.0.3
iptables --table nat --insert POSTROUTING 1 --source 172.20.0.3 --jump SNAT --to-source 172.30.133.255
pct start 202
pct push 202 /root/honey.tar /root/honey.tar
pct push 202 /root/sshd_config /etc/ssh/sshd_config
pct exec 202 service ssh restart
pct exec 202 -- tar -xvf honey.tar
pct exec 202 -- rm honey.tar
pct exec 202 -- cp -r honey/. /home
pct exec 202 -- rm -rf honey
pct exec 202 -- apt update
pct exec 202 -- wget -O snoopy-install.sh https://github.com/a2o/snoopy/raw/install/doc/install/bin/snoopy-install.sh
pct exec 202 -- chmod 755 snoopy-install.sh
pct exec 202 -- /root/snoopy-install.sh stable
pct stop 202
iptables --table nat --delete PREROUTING --destination 172.30.133.255 --jump DNAT --to-destination 172.20.0.3
iptables --table nat --delete POSTROUTING --source 172.20.0.3 --jump SNAT --to-source 172.30.133.255
pct template 202
