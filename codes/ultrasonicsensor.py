# coding:utf-8

import sys
import time
import signal
import RPi.GPIO as GPIO

def clean():
    GPIO.cleanup()

def sigint_handler(signum, instant):
    clean()
    sys.exit()

signal.signal(signal.SIGINT, sigint_handler)

TRIGdir = 40
ECHOdir = 38
TRIGcen = 36
ECHOcen = 32
TRIGesq = 37
ECHOesq = 35

sampling_rate = 20.0
speed_of_sound = 343
max_distance = 4.0
max_delta_t = max_distance / speed_of_sound

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)   
GPIO.setup(TRIGdir, GPIO.OUT)
GPIO.setup(ECHOdir, GPIO.IN)
GPIO.setup(TRIGcen, GPIO.OUT)
GPIO.setup(ECHOcen, GPIO.IN)
GPIO.setup(TRIGesq, GPIO.OUT)
GPIO.setup(ECHOesq, GPIO.IN)

GPIO.output(TRIGdir, False)
time.sleep(1)
GPIO.output(TRIGcen, False)
time.sleep(1)
GPIO.output(TRIGesq, False)
time.sleep(1)

print ("Sampling Rate:", sampling_rate, "Hz")
print ("Distances (cm)")

def getDistance(trig, echo):
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

    return distance

while True:
    print(round(getDistance(TRIGdir, ECHOdir), 2), "dir", round(getDistance(TRIGcen, ECHOcen), 2), "cen", round(getDistance(TRIGesq, ECHOesq), 2), "esq")
    time.sleep(1)