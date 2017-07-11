#!/bin/bash
screen -p sensor -X stuff "python /home/pi/workspace/bitcoin-miner/read-to-db.py $(printf \\r)"
