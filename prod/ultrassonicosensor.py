# coding:utf-8

import sys
import time
import signal
import RPi.GPIO as GPIO

from queue import Queue

queueRight = Queue()
queueCentral = Queue()
queueLeft = Queue()

def clean():
    GPIO.cleanup()

def sigint_handler(signum, instant):
    clean()
    sys.exit()

signal.signal(signal.SIGINT, sigint_handler)

sampling_rate = 20.0
speed_of_sound = 343
max_distance = 4.0
max_delta_t = max_distance / speed_of_sound
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def getDistance(_id):

    if _id == 1:
        trig = 21
        echo = 20
    elif _id == 2:
        trig = 16
        echo = 12
    elif _id == 3:
        trig = 26
        echo = 19
    else: return None

    while True:
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

        GPIO.output(trig, False)
        time.sleep(1)

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echo) == 0:
            start_t = time.time()

        while GPIO.input(echo) == 1 and time.time() - start_t < max_delta_t:
            end_t = time.time()

        if end_t - start_t < max_delta_t:
            delta_t = end_t - start_t
            distance = 100*(0.5 * delta_t * speed_of_sound)
        else:
            distance = -1

        if _id == 1:
            queueRight.put(round(distance, 2))
        elif _id == 2:
            queueCentral.put(round(distance, 2))
        elif _id == 3:
            queueLeft.put(round(distance, 2))
        else: return None

        #return round(distance, 2)
