#!/usr/bin/python

import RPi.GPIO as GPIO
from lib.Adafruit_PWM_Servo_Driver import PWM
from lib import xbox_read

# Initialise the PWM servo driver using the default address, there are pins you can solder shut, for when you have several contollers.
pwm = PWM(0x40, debug=True)

# Default calibration values 
servoDrive = 425 #max turn speed of the servo
servoDriveWidth = 360 #kind of servo, 360 is continuous rotation servo
servoSteer = 425 #max turn speed of the servo
servoSteerWidth = 180 #kind of servo, 180 is 180 degrees rotation servo

pwm.setPWMFreq(60) # Set frequency to 60 Hz

# set the names and values of the servos
drive = servoDrive
steer = servoSteer

for event in xbox_read.event_stream(deadzone=12000):
    # left thumbstick controls the speed
    if event.key=='Y1':
        # if your servo turns the wrong way, add a minus in front of: 32768 so it would be */-32768
        drive = int( servoDrive + (servoDriveWidth*-event.value)/32768 )
        pwm.setPWM(0, 0, drive)
    # Right thumbstick controls the steering
    if event.key=='X2':
        # if your servo turns the wrong way, add a minus in front of: 32768 so it would be */-32768
        steer = int( servoSteer + (servoSteerWidth*-event.value)/32768 )
        pwm.setPWM(1, 0, steer)
