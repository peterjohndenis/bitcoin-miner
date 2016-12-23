import subprocess, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,V GPIO.OUT)

subprocess.call("./stop-cgminer.sh")
time.sleep(5)
GPIO.output(7, False)
