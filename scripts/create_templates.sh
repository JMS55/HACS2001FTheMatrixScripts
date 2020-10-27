pct unmount 101
pct destroy 101

pct unmount 102
pct destroy 102

pct unmount 103
pct destroy 103

pct destroy 201
pct create 201 /var/lib/vz/template/cache/ubuntu-16.04-standard_16.04.5-1_amd64.tar.gz --storage local-lvm --net0 name=eth0,ip=172.20.0.2/16,bridge=vmbr0,gw=172.20.0.1 -hostname backup
pct start 201
pct push 201 /root/honey.tar /home/honey.tar
pct push 201 /root/sshd_config /home/sshd_config
pct exec 201 -- cd /home && tar -xvf honey.tar && rm honey.tar && cp -R honey/* . && rm -rf honey
pct exec 201 -- cd /home && cp sshd_config /etc/ssh
pct exec 201 echo -e "123" | passwd root
pct stop 201
pct template 201

pct destroy 202
pct create 202 /var/lib/vz/template/cache/ubuntu-16.04-standard_16.04.5-1_amd64.tar.gz --storage local-lvm --net0 name=eth0,ip=172.20.0.3/16,bridge=vmbr0,gw=172.20.0.1 -hostname backup
iptables --table nat --insert PREROUTING 1 --destination 172.30.133.255 --jump DNAT --to-destination 172.20.0.3
iptables --table nat --insert POSTROUTING 1 --source 172.20.0.3 --jump SNAT --to-source 172.30.133.255
pct start 202
pct push 202 /root/honey.tar /home/honey.tar
pct push 202 /root/sshd_config /home/sshd_config
pct exec 202 -- cd /home && tar -xvf honey.tar && rm honey.tar && cp -R honey/* . && rm -rf honey
pct exec 202 -- cd /home && cp sshd_config /etc/ssh
pct exec 202 echo -e "123" | passwd root
pct exec 202 -- apt update
pct exec 202 -- wget -O snoopy-install.sh https://github.com/a2o/snoopy/raw/install/doc/install/bin/snoopy-install.sh && chmod 755 snoopy-install.sh && ./snoopy-install.sh stable
pct stop 202
iptables --table nat --delete PREROUTING --destination 172.30.133.255 --jump DNAT --to-destination 172.20.0.3
iptables --table nat --delete POSTROUTING --source 172.20.0.3 --jump SNAT --to-source 172.30.133.255
pct template 202
