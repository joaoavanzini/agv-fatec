import RPi.GPIO as io 
import time, os

io.setmode(io.BCM)
io.setwarnings(False)

in1 = 24
in2 = 23
in3 = 17 
in4 = 27
Apwm = 25
Bpwm = 22

io.setup(in1, io.OUT)
io.setup(in2, io.OUT)
io.setup(in3, io.OUT)
io.setup(in4, io.OUT)

io.setup(Apwm, io.OUT)
io.setup(Bpwm, io.OUT)

pwm1 = io.PWM(Apwm,100)
pwm2 = io.PWM(Bpwm,100)

io.output(in1, io.LOW)
io.output(in2, io.LOW)
io.output(in3, io.LOW)
io.output(in4, io.LOW)

pwm1.start(0)
pwm2.start(0)
pwm1.ChangeDutyCycle(0)
pwm2.ChangeDutyCycle(0)

def setMotorMode(mode, pwm):
    if(mode == 1):
        print("forward")
        io.output(in1, io.HIGH)
        io.output(in2, io.LOW)
        io.output(in3, io.HIGH)
        io.output(in4, io.LOW)
        pwm1.ChangeDutyCycle(pwm)
        pwm2.ChangeDutyCycle(pwm)
    elif(mode == 2):
         print("backward")
         io.output(in1, io.LOW)
         io.output(in2, io.HIGH)
         io.output(in3, io.LOW)
         io.output(in4, io.HIGH)
         pwm1.ChangeDutyCycle(pwm)
         pwm2.ChangeDutyCycle(pwm)
    elif(mode == 3):
        print("stop")
        io.output(in1, io.LOW)
        io.output(in2, io.LOW)
        io.output(in3, io.LOW)
        io.output(in4, io.LOW) 
    elif(mode == 4):
        print("left")
        io.output(in1, io.HIGH)
        io.output(in2, io.HIGH) 
        pwm1.ChangeDutyCycle(pwm)
        pwm2.ChangeDutyCycle(pwm)
    elif(mode == 5):
        print("right")
        io.output(in3, io.HIGH)
        io.output(in4, io.HIGH)  
        pwm1.ChangeDutyCycle(pwm)
        pwm2.ChangeDutyCycle(pwm)
    else:
        print("else-stop")
        io.output(in1, io.LOW)
        io.output(in2, io.LOW)
        io.output(in3, io.LOW)
        io.output(in4, io.LOW) 