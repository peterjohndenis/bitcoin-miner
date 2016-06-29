import subprocess, time, json, MySQLdb

with open('./mysql_config.json') as config_file:
    conf = json.load(config_file)

def conn_fetch():
	# connect to database
	db = MySQLdb.connect(host=conf["host"],     # your host, usually localhost
		             user=conf["login"],    # your username
		             passwd=conf["passwd"], # your password
		             db=conf["database"])   # name of the data base             
	# create cursor-object
	cur = db.cursor()
	# execute query and fetch
	cur.execute("SELECT voltage FROM sensor_data ORDER BY id DESC LIMIT 1")
	value = cur.fetchone()[0]
	# close connection to database
	cur.close()
	db.close()
	return value

subprocess.call(["screen", "-t", "cgminer"])
minutes = 15
seconds = minutes * 60 

while True
	flag = True
	while flag:
		voltValue = conn_fetch()
		if voltValue >= 13.5:
			flag = False
		else:
			time.sleep(seconds)
		
	#run cg-miner
	#stop_sleep.sh
	subprocess.call("./run-cgminer.sh")

	flag = True
	while flag:
		voltValue = conn_fetch()
		if voltValue <= 12.0:
		        flag = False
		else:
		        time.sleep(seconds)

	#stop cg-miner
	subprocess.call("./stop-cgminer.sh")
	#start_sleep.sh
