# coding:utf-8
import RPi.GPIO as GPIO
import time
import json
import paho.mqtt.client as mqtt
import bridgeMotor as Motor

from threading import Thread
from queue import Empty

import ultrassonicosensor as ultra

from datetime import datetime

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
                now = datetime.now()
                getJsonRightUltra = {"value:": valueRight, "type:":"cm", "position:":"Right", "datetime:": now.strftime("%d/%m/%Y %H:%M:%S")}
                getJsonRightUltra = json.dumps(getJsonRightUltra)
                sendData("agv/sensor/ultra/right", getJsonRightUltra)
                valueRight = 0
            
            try:
                valueCentral = ultra.queueCentral.get_nowait()
            except Empty:
                pass
            else:
                now = datetime.now()
                getJsonCentralUltra = {"value:": valueCentral, "type:":"cm", "position:":"Central", "datetime:": now.strftime("%d/%m/%Y %H:%M:%S")}
                getJsonCentralUltra = json.dumps(getJsonCentralUltra)
                sendData("agv/sensor/ultra/central", getJsonCentralUltra)
                valueCentral = 0
            
            try:
                valueLeft = ultra.queueLeft.get_nowait()
            except Empty:
                pass
            else:
                now = datetime.now()
                getJsonLeftUltra = {"value:": valueLeft, "type:":"cm", "position:":"Left", "datetime:": now.strftime("%d/%m/%Y %H:%M:%S")}
                getJsonLeftUltra = json.dumps(getJsonLeftUltra)               
                sendData("agv/sensor/ultra/left", getJsonLeftUltra)
                valueLeft = 0


            leftLine = GPIO.input(leftLineSensor)
            rightLine = GPIO.input(rightLineSensor)
            now = datetime.now()
            
            # segue a linha

            #print("leftLine = ", leftLine, "rightLine = ", rightLine)
            getJsonLiner = {"leftLine:": leftLine, "rightLine:": rightLine, "datetime:": now.strftime("%d/%m/%Y %H:%M:%S")}
            getJsonLiner = json.dumps(getJsonLiner)
            sendData("agv/sensor/linha", getJsonLiner)

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