import subprocess, time, json, MySQLdb, datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, False)
subprocess.call(["sudo", "./sleep.sh"])

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
	values = cur.fetchall()
	# close connection to database
	cur.close()
	db.close()
	return values

subprocess.call(["screen", "-t", "cgminer"])
minutes = 15
seconds = minutes * 60 

while True:
	flag = True
	while flag:
		voltValues = conn_fetch()
		#print datetime.datetime.now().time(), " ", voltValue
		if voltValues[0][0] >= 13.5 && voltValues[1][0] >= 13.5:
			flag = False
		else:
			time.sleep(seconds)
		
	#run cg-miner
	subprocess.call(["sudo", "./wakeup.sh"])
	time.sleep(10)
	GPIO.output(7, True)
	time.sleep(1)
	subprocess.call("./run-cgminer.sh")

	flag = True
	while flag:
		voltValue = conn_fetch()
		#print datetime.datetime.now().time(), " ", voltValue
		if voltValue <= 11.7:
		        flag = False
		else:
		        time.sleep(seconds)

	#stop cg-miner
	subprocess.call("./stop-cgminer.sh")
	time.sleep(5)
	GPIO.output(7, False)
	subprocess.call(["sudo", "./sleep.sh"])
