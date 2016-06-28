import plotly.plotly as py
import json
import time
import readadc
import datetime

with open('./plotly_config.json') as config_file:
    plotly_user_config = json.load(config_file)

py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

url = py.plot([
    {
        'x': [], 'y': [], 'type': 'scatter',
        'stream': {
            'token': plotly_user_config['plotly_streaming_tokens'][1],
            'maxpoints': 500
        }
    }], filename='Voltage monitor')

print "View your streaming graph here: ", url

# temperature sensor middle pin connected channel 1 of mcp3008
sensor_pin = 1
readadc.initialize()

stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][1])
stream.open()

#the main sensor reading and plotting loop
while True:
	sensor_data = readadc.readadc(sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, readadc.PINS.SPICS)

	millivolts = sensor_data * (3300.0 / 1024.0)
	
	# convert volts to original input
	millivolts = millivolts * 4.5 + 280
	
	# convert millivolts to volts
	volts = millivolts / 1000

	# remove decimal point from millivolts
	millivolts = "%d" % millivolts
	
	# show only one decimal place for voltage readings
	volts = "%.1f" % volts

	# write the data to plotly
	stream.write({'x': datetime.datetime.now(), 'y': volts})

	# delay between stream posts,
	time.sleep(45)
	""""for i in range(30):
		time.sleep(30)
		stream.write('')
		time.sleep(30)"""
