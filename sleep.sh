#!/bin/bash
#Code to stop
/etc/init.d/networking stop
echo 0 > /sys/devices/platform/soc/20980000.usb/buspower
sleep 2
#echo “Bus power stopping”

