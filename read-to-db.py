import MySQLdb
import json
import time
import readadc
#import datetime

with open('./mysql_config.json') as config_file:
    conf = json.load(config_file)

# Sensors connected to channel 0 and 1 of mcp3008
temp_sensor_pin = 0
volt_sensor_pin = 1
readadc.initialize()


#the main sensor reading and plotting loop
while True:

	# voltage
	volt_sensor_data = readadc.readadc(volt_sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, readadc.PINS.SPICS)
	# convert data to millivolt
	millivolts = volt_sensor_data * (3300.0 / 1024.0)
	# convert volts to original input
	millivolts = millivolts * 4.5 + 280
	# convert millivolts to volts
	volts = millivolts / 1000
	# remove decimal point from millivolts // this is only used for debug
	millivolts = "%d" % millivolts
	# show only one decimal place for voltage readings
	volts = "%.1f" % volts

	# temperature
	temp_sensor_data = readadc.readadc(temp_sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, readadc.PINS.SPICS)
	# convert data to millivolt
	temp_millivolts = temp_sensor_data * (3300.0 / 1024.0)
        # 10 mv per degree
        temp_C = (temp_millivolts - 500.0) / 10
        # remove decimal point from millivolts // this only is used for debug
        temp_millivolts = "%d" % temp_millivolts
        # show only one decimal place for temperature
        temp_C = "%.1f" % temp_C

	# connect to database
	db = MySQLdb.connect(host=conf["host"],    # your host, usually localhost
                     user=conf["login"],         # your username
                     passwd=conf["passwd"],  # your password
                     db=conf["database"])        # name of the data base

	# Create cursor-object
	cur = db.cursor()
		
	# write data to mysql
	params = [temp_C, volts, time.mktime(time.localtime())] #datetime.datetime.now()
	try:
		cur.execute("INSERT INTO sensor_data (temp, voltage, localtime) VALUES (%s, %s, %s)", params)
	except MySQLdb.Error, e:
		try:
			print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
		except IndexError:
			print "MySQL Error: %s" % str(e)
	
	cur.close()
	db.commit()	
	db.close()

	# delay between database posts,
	minutes = 15
	seconds = minutes * 60
	time.sleep(seconds)


