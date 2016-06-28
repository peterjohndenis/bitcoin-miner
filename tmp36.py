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
            'token': plotly_user_config['plotly_streaming_tokens'][0],
            'maxpoints': 100
        }
    }], filename='Raspberry Pi Streaming Example Values')

print "View your streaming graph here: ", url

# temperature sensor middle pin connected channel 0 of mcp3008
sensor_pin = 0
readadc.initialize()

stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][0])
stream.open()

#the main sensor reading and plotting loop
while True:
	sensor_data = readadc.readadc(sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, readadc.PINS.SPICS)
	
	millivolts = sensor_data * (3300.0 / 1024.0)
	# 10 mv per degree
	temp_C = (millivolts - 500.0) / 10
	# remove decimal point from millivolts
	millivolts = "%d" % millivolts
	# show only one decimal place for temperature
	temp_C = "%.1f" % temp_C
	
	# write the data to plotly
	stream.write({'x': datetime.datetime.now(), 'y': temp_C})
	
	# delay between stream posts
	for i in range(30):
		time.sleep(30)
		stream.write('')
		time.sleep(30)
