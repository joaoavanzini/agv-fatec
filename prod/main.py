# coding:utf-8
import RPi.GPIO as GPIO
import time
import json
import paho.mqtt.client as mqtt
import bridgeMotor as Motor

from threading import Thread
from queue import Empty

import ultrassonicosensor as ultra

leftLineSensor = 5
rightLineSensor = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(leftLineSensor, GPIO.IN)
GPIO.setup(rightLineSensor, GPIO.IN)

client = mqtt.Client("AGV")

def destroy():
     GPIO.cleanup()

def sendData(topic, message):
    client.connect("192.168.15.178", 1883, 60)
    #client.publish("agv/linha", x)
    client.publish(topic, message)

if __name__ == '__main__':

    Thread(target=ultra.getDistance, daemon=True, args=[1]).start()
    Thread(target=ultra.getDistance, daemon=True, args=[2]).start()
    Thread(target=ultra.getDistance, daemon=True, args=[3]).start()

    try:
        while True:
            
            try:
                valueRight = ultra.queueRight.get_nowait()
            except Empty:
                pass
            else:
                sendData("agv/ultra/right", valueRight)
            
            try:
                valueCentral = ultra.queueCentral.get_nowait()
            except Empty:
                pass
            else:
                sendData("agv/ultra/central", valueCentral)
            
            try:
                valueLeft = ultra.queueLeft.get_nowait()
            except Empty:
                pass
            else:
                sendData("agv/ultra/left", valueLeft)


            leftLine = GPIO.input(leftLineSensor)
            rightLine = GPIO.input(rightLineSensor)

            print("leftLineft = ", leftLine, "right = ", rightLine)
            getJsonLiner = {"leftLineft: ": leftLine, "right: ": rightLine}
            getJsonLiner = json.dumps(getJsonLiner)

            sendData("agv/linha", getJsonLiner)

            Motor.setMotorMode(1, 100)
            if (leftLine == 0 and rightLine == 1):
                Motor.setMotorMode(4, 100)
                leftLine = GPIO.input(leftLineSensor)
                rightLine = GPIO.input(rightLineSensor)


            if (rightLine == 0 and leftLine == 1):
                Motor.setMotorMode(5, 100)
                leftLine = GPIO.input(leftLineSensor)
                rightLine = GPIO.input(rightLineSensor)


    except KeyboardInterrupt:
        Motor.setMotorMode(3, 0)
        print("Stopped by user")
        client.disconnect()
        destroy()
        
