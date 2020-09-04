import time
import RPi.GPIO as GPIO

eSensor = 5
dSensor = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dSensor, GPIO.IN)
GPIO.setup(eSensor, GPIO.IN)

def read_sensors():
    global lf1, lf2
    lf1 = GPIO.input(eSensor)
    lf2 = GPIO.input(dSensor)

def destroy():
    GPIO.cleanup()

def main():
    while True:
        read_sensors()

        print("esq = ", lf1, "dir = ", lf2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        #robot car stop
        destroy()