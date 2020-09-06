import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import json

eSensor = 5
dSensor = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dSensor, GPIO.IN)
GPIO.setup(eSensor, GPIO.IN)

client = mqtt.Client()

def read_sensors():
    global lf1, lf2
    lf1 = GPIO.input(eSensor)
    lf2 = GPIO.input(dSensor)

def destroy():
    GPIO.cleanup()

def sentData(x):
    client.connect("192.168.15.178", 1883, 60)
    client.publish("agv/linha", x)
    time.sleep(1)

def main():
    while True:
        read_sensors()
        x = {"dir:": lf1, "esq": lf2}
        x = json.dumps(x)
        sentData(x)
        print("esq = ", lf1, "dir = ", lf2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        client.disconnect()
        #robot car stop
        destroy()