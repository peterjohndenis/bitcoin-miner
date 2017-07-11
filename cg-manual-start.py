import subprocess, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)
time.sleep(1)

subprocess.call(["screen", "-Sdm", "bitcoin", "-t", "cgminer"])
subprocess.call(["screen", "-S", "bitcoin", "-X", "screen", "-t", "sensor"])
subprocess.call("/home/pi/workspace/bitcoin-miner/run-sensor.sh")
subprocess.call("/home/pi/workspace/bitcoin-miner/run-cgminer.sh")
