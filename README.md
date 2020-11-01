# HACS200 Group 1F - TheMatrix

## Host VM Login
* To SSH into the HostVM: `ssh root@jump.aces.umd.edu -p15831`
* Username: `root`
* Password: `1fmatrix`

## Setup Files
1. `git clone https://github.com/JMS55/HACS2001FTheMatrixScripts`
2. `cp HACS2001FTheMatrixScripts/scripts/* /root && chmod a+x /root/*.sh`
3. `cp HACS2001FTheMatrixScripts/honey/honey.tar /root`
4. `cp HACS2001FTheMatrixScripts/configs/sshd_config /root`
5. `cp HACS2001FTheMatrixScripts/configs/rc.local /etc && chmod a+x /etc/rc.local`
6. `cp HACS2001FTheMatrixScripts/configs/mitm_config.js /root/MITM/config`
7. `/root/MITM/install.sh`

## Health Logs
* Add healthLogs to `/etc/cron.hourly`

## Finishing
Reboot to finish
