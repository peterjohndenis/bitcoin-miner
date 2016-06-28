#!/bin/bash
screen -d -m -S bcmine -t cgminer

screen -S bcmine -X stuff "./run-cgminer.sh $(printf \\r)"

screen -S bcmine -X screen -t tmp36
screen -S bcmine -p tmp36 -X stuff "python tmp36.py $(printf \\r)"

screen -S bcmine -X screen -t v12
screen -S bcmine -p v12 -X stuff "python v12.py $(printf \\r)"
