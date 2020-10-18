# HACS200 Group 1F - TheMatrix

## Host VM Login
* To SSH into the HostVM: `ssh root@jump.aces.umd.edu -p15831`
* Username: `root`
* Password: `1fmatrix`

## Setting up the SDI From Scratch
1. Setup necessary files
    1. `git clone https://github.com/JMS55/HACS2001FTheMatrixScripts`
    2. `chmod +x HACS2001FTheMatrixScripts/scripts/*`
    3. `cp HACS2001FTheMatrixScripts/scripts/* /root`
    4. `cp HACS2001FTheMatrixScripts/scripts/* /root`
    5. `cp HACS2001FTheMatrixScripts/configs/mitm_config.js /root/MITM/config`
    6. `/root/MITM/install.sh`
1. Setup networking
    1. `ip addr add 128.8.37.122/255.255.0.0 dev enp4s1`
    2. `sysctl -w net.ipv4.ip_forward=1`
    3. `iptables --table nat --append PREROUTING --source 0.0.0.0/0 --destination 128.8.37.122 --jump DNAT --to-destination 172.20.0.2`
    4. `iptables --table nat --append PREROUTING --source 0.0.0.0/0 --destination 128.8.37.122 --jump DNAT --to-destination 172.20.0.3`
    5. `iptables --table nat --append POSTROUTING --source 172.20.0.2 --destination 0.0.0.0/0 --jump SNAT --to-source 128.8.37.122`
    6. `iptables --table nat --append POSTROUTING --source 172.20.0.3 --destination 0.0.0.0/0 --jump SNAT --to-source 128.8.37.122`
    7. `iptables --table nat --insert PREROUTING 1 --destination 128.8.37.122 --protocol tcp --destination-port 22 --jump DNAT --to-destination 172.20.0.1:10000`

## Creating Container Templates
* Control:
    * `pct create 201 /var/lib/vz/template/cache/ubuntu-16.04-standard_16.04.5-1_amd64.tar.gz --storage local-lvm --net0 name=eth0,ip=172.20.0.2/16,bridge=vmbr0,gw=172.20.0.1`
    * `pct start 201`
    * `pct push 201 /root/honey.tar /root`
    * `pct enter`
    * `tar -xvf honey.tar && rm honey.tar`
    * `exit`
    * `pct stop 201`
    * `pct template 201`
* Experimental (Snoopy)
    * `pct create 202 /var/lib/vz/template/cache/ubuntu-16.04-standard_16.04.5-1_amd64.tar.gz --storage local-lvm --net0 name=eth0,ip=172.20.0.2/16,bridge=vmbr0,gw=172.20.0.1`
    * **TODO**: Give container internet access
    * `pct start 202`
    * `pct push 202 /root/honey.tar /root`
    * `pct enter`
    * `tar -xvf honey.tar && rm honey.tar`
    * `wget -O snoopy-install.sh https://github.com/a2o/snoopy/raw/install/doc/install/bin/snoopy-install.sh && chmod 755 snoopy-install.sh && ./snoopy-install.sh stable`
    * `exit`
    * `pct stop 202`
    * **TODO**: Revoke container internet access
    * `pct template 202`

## Starting Scripts
Run `nohup /root/start.sh &`
