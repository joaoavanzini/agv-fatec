# coding:utf-8
import RPi.GPIO as GPIO
import time
import bridgeMotor as Motor

if __name__ == '__main__':
    try:
        while True:
            Motor.setMotorMode(1, 100)
            time.sleep(5)
            Motor.setMotorMode(4, 100)
            time.sleep(5)
            Motor.setMotorMode(1, 100)
            time.sleep(5)
            Motor.setMotorMode(5, 100)
            time.sleep(5)
            Motor.setMotorMode(2, 100)
            time.sleep(5)
            Motor.setMotorMode(3, 100)
            time.sleep(5)
    except KeyboardInterrupt:
        Motor.setMotorMode(3, 0)
        print("Stooped by user")
        
