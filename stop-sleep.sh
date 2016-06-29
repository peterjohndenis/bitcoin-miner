#!/bin/bash
#Code to start
echo 1 > /sys/devices/platform/soc/20980000.usb/buspower;
#echo “Bus power starting”
sleep 2;
/etc/init.d/networking start

#open relay
