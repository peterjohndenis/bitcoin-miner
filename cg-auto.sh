#!/bin/bash
trap "exit" INT
screen -t cgminer
while true
do

#################################################################################

python <<END_OF_PYTHON
import time
import MySQLdb
import json

with open('./mysql_config.json') as config_file:
    conf = json.load(config_file)


flag = True
min = 15
seconds = min * 60 
while flag:
	# connect to database
	db = MySQLdb.connect(host=conf["host"],     # your host, usually localhost
                     user=conf["login"],    # your username
                     passwd=conf["passwd"], # your password
                     db=conf["database"])   # name of the data base

	# create cursor-object
	cur = db.cursor()

	# execute query and fetch
	cur.execute("SELECT voltage FROM sensor_data ORDER BY id DESC LIMIT 1")
	voltValue = cur.fetchone()[0]
	if voltValue >= 13.5:
		flag = False
		# close connection to database
		cur.close()
		db.close()

	else:
		time.sleep(seconds)
		# close connection to database
		cur.close()
		db.close()

END_OF_PYTHON

#################################################################################

screen -p cgminer -X stuff "./run-cgminer.sh $(printf \\r)"

#################################################################################

python <<END_OF_PYTHON
import time
import MySQLdb
import json

with open('./mysql_config.json') as config_file:
    conf = json.load(config_file)

flag = True
min = 15
seconds = min * 60
while flag:
        # connect to database
        db = MySQLdb.connect(host=conf["host"],     # your host, usually localhost
                     user=conf["login"],    # your username
                     passwd=conf["passwd"], # your password
                     db=conf["database"])   # name of the data base

        # create cursor-object
        cur = db.cursor()

        # execute query and fetch
        cur.execute("SELECT voltage FROM sensor_data ORDER BY id DESC LIMIT 1")
        voltValue = cur.fetchone()[0]
        if voltValue <= 12.0:
                flag = False
                # close connection to database
                cur.close()
                db.close()

        else:
                time.sleep(seconds)
                # close connection to database
                cur.close()
                db.close()

END_OF_PYTHON

#################################################################################

screen -p cgminer -X stuff "q"

done
