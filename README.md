# HACS200 Group 1F - TheMatrix

## Host VM Login
* To SSH into the HostVM: `ssh root@jump.aces.umd.edu -p15831`
* Username: `root`
* Password: `1fmatrix`

## Setup Files
1. `git clone https://github.com/JMS55/HACS2001FTheMatrixScripts`
2. `cp HACS2001FTheMatrixScripts/scripts/* /root && chmod a+x /root/*.sh`
3. `cp /root/health_logs.sh /etc/cron.hourly`
4. `cp HACS2001FTheMatrixScripts/honey/honey.tar /root`
5. `cp HACS2001FTheMatrixScripts/configs/sshd_config /root`
6. `cp HACS2001FTheMatrixScripts/configs/rc.local /etc && chmod a+x /etc/rc.local`
7. `cp HACS2001FTheMatrixScripts/configs/mitm_config.js /root/MITM/config`
8. `/root/MITM/install.sh`

## Finishing
Reboot to finish

## Restarting Scripts When MITM Breaks
1. `ps aux | grep .sh`, note down the process ID's of monitor.sh (don't kill other scripts)
2. Do the above for all `node` and `tail` processes
3. `kill -9 <process id>` for each process
4. `pct stop/unmount/destroy` for all 10X containers (NOT 201/202). Do those 3 commands in that order for each container
5. Look at rc.local, and do `nohup <command>` for each of the commands about starting each container
