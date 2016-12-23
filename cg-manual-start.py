import subprocess, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)
time.sleep(1)

subprocess.call(["screen", "-t", "cgminer"])
subprocess.call("./run-cgminer.sh")
