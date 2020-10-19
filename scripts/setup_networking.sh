ip addr add 128.8.37.122/255.255.0.0 dev enp4s1

sysctl -w net.ipv4.ip_forward=1

iptables --table nat --append PREROUTING --destination 128.8.37.122 --protocol tcp --destination-port 22 --jump DNAT --to-destination 172.20.0.1:10000
iptables --table nat --append PREROUTING --source 0.0.0.0/0 --destination 128.8.37.122 --jump DNAT --to-destination 172.20.0.2
iptables --table nat --append PREROUTING --source 0.0.0.0/0 --destination 128.8.37.122 --jump DNAT --to-destination 172.20.0.3
iptables --table nat --append POSTROUTING --source 172.20.0.2 --destination 0.0.0.0/0 --jump SNAT --to-source 128.8.37.122
iptables --table nat --append POSTROUTING --source 172.20.0.3 --destination 0.0.0.0/0 --jump SNAT --to-source 128.8.37.122

/root/Honeypot_Project/firewall/firewall_rules.sh
