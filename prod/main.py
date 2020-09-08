# coding:utf-8
import RPi.GPIO as GPIO
import time
import json
import paho.mqtt.client as mqtt
import bridgeMotor as Motor

from threading import Thread
from queue import Empty

import ultrassonicosensor as U

leSensor = 5
reSensor = 13

# 1
TRIGdir = 21
ECHOdir = 20

# 2
TRIGcen = 16
ECHOcen = 12

# 3
TRIGesq = 26
ECHOesq = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(leSensor, GPIO.IN)
GPIO.setup(reSensor, GPIO.IN)

client = mqtt.Client("AGV")

def destroy():
     GPIO.cleanup()

def sendData(topic, message):
    client.connect("192.168.15.178", 1883, 60)
    #client.publish("agv/linha", x)
    client.publish(topic, message)

if __name__ == '__main__':

    Thread(target=U.getDistance, daemon=True, args=[1]).start()
    Thread(target=U.getDistance, daemon=True, args=[2]).start()
    Thread(target=U.getDistance, daemon=True, args=[3]).start()

    try:
        while True:
            
            try:
                val1 = U.queue1.get_nowait()
            except Empty:
                pass
            else:
                sendData("agv/ultra/dir", val1)
            
            try:
                val2 = U.queue2.get_nowait()
            except Empty:
                pass
            else:
                sendData("agv/ultra/cen", val2)
            
            try:
                val3 = U.queue3.get_nowait()
            except Empty:
                pass
            else:
                sendData("agv/ultra/esq", val3)


            le = GPIO.input(leSensor)
            re = GPIO.input(reSensor)

            print("left = ", le, "right = ", re)
            getJsonLiner = {"left: ": le, "right: ": re}
            getJsonLiner = json.dumps(getJsonLiner)

            sendData("agv/linha", getJsonLiner)

            Motor.setMotorMode(1, 100)
            if (le == 0 and re == 1):
                Motor.setMotorMode(4, 100)
                le = GPIO.input(leSensor)
                re = GPIO.input(reSensor)


            if (re == 0 and le == 1):
                Motor.setMotorMode(5, 100)
                le = GPIO.input(leSensor)
                re = GPIO.input(reSensor)


    except KeyboardInterrupt:
        Motor.setMotorMode(3, 0)
        print("Stopped by user")
        client.disconnect()
        destroy()
        
