# HACS200 Group 1F - TheMatrix

## Host VM Login
* To SSH into the HostVM: `ssh root@jump.aces.umd.edu -p15831`
* Username: `root`
* Password: `2fmatrix`

## Setting up the SDI From Scratch
1. `git clone https://github.com/JMS55/HACS2001FTheMatrixScripts`
2. `cp HACS2001FTheMatrixScripts/scripts/* /root`
3. `cp HACS2001FTheMatrixScripts/configs/mitm_config.js /root`
4. `./MITM/install.sh`
5. Send attackers through MITM `iptables --table nat --insert PREROUTING 1 --destination 128.8.37.122 --protocol tcp --destination-port 22 --jump DNAT --to-destination 172.20.0.1:10000`

## Creating Container Templates
**TODO**: Add honey to both
* Control:
    * `pct create 201 /var/lib/vz/template/cache/ubuntu-16.04-standard_16.04.5-1_amd64.tar.gz --storage local-lvm --net0 name=eth0,ip=172.20.0.2/16,bridge=vmbr0,gw=172.20.0.1`
    * `pct template 201`
* Experimental (snoopy)
    * `pct create 202 /var/lib/vz/template/cache/ubuntu-16.04-standard_16.04.5-1_amd64.tar.gz --storage local-lvm --net0 name=eth0,ip=172.20.0.2/16,bridge=vmbr0,gw=172.20.0.1`
    * **TODO**: Give container internet access
    * `pct start 202`
    * `pct enter`
    * `wget -O snoopy-install.sh https://github.com/a2o/snoopy/raw/install/doc/install/bin/snoopy-install.sh && chmod 755 snoopy-install.sh && ./snoopy-install.sh stable`
    * `exit`
    * `pct stop 202`
    * **TODO**: Revoke container internet access
    * `pct template 202`

## Starting Scripts
Run `nohup ./start.sh` from `/root`
