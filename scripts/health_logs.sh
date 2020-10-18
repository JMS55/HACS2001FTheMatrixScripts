#!/bin/bash

file=$(date '+%d/%m/%Y %H:%M:%S')

echo $(date '+%d/%m/%Y %H:%M:%S') >> file

echo "\n HOST: \n" >> file
echo $(free --mega) >> file
echo "\n" >> file
echo $(df) >> file
echo "\n" >> file
echo $(uptime) >> file
echo "\n" >> file
echo $(vnstat) >> file


echo "\n CONTROL: \n" >> file
echo $(pct exec 101 free --mega) >> file
echo "\n" >> file
echo $(pct exec 101 df) >> file
echo "\n" >> file
echo $(pct exec 101 uptime) >> file
echo "\n" >> file
echo $(pct exec 101 vnstat) >> file


echo "\n SNOOPY: \n" >> file
echo $(pct exec 102 free --mega) >> file
echo "\n" >> file
echo $(pct exec 102 df) >> file
echo "\n" >> file
echo $(pct exec 102 uptime) >> file
echo "\n" >> file
echo $(pct exec 102 vnstat) >> file


mv file health_logs
rm file

sleep 1h
health_logs.sh
