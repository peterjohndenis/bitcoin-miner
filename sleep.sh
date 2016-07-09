#!/bin/bash
#Code to stop
echo “Bus power stopping”
/etc/init.d/networking stop
echo 0 > /sys/devices/platform/soc/20980000.usb/buspower;

