#!/bin/bash
screen -p cgminer -X stuff "sudo ~/bitcoin/cgminer/cgminer --bmsc-options 115200:0.57 -o stratum+tcp://eu.stratum.bitcoin.cz:3333 -u Ejdamm.antminerU3 -p qwerty --bmsc-voltage 0800 --bmsc-freq 1286 $(printf \\r)"
