# Lego-pi
My version of the lego pi car from Tom Rees, uses two servos instead of one servo and a different motor. All credit goes to him!

HOW TO: Build an RC Car using Lego and a Raspberry Pi
Parts list (I bought everything from a local shop, this is just for reference, I only ordered the Adafruit driver from the Adafruit website)
The parts at least necessary for this project are as following:
1Raspberry pi B/B+ (you can find them all over)
1Adafruit 16-Channel 12-bit PWM/Servo Driver - I2C interface - PCA9685 (this is the servo       controller)
1 Servo motor for driving (http://www.robotshop.com/en/hitec-hs422-servo-motor.html) 
1 Servo motor for steering (http://www.robotshop.com/en/gws-naro-servo-motor.html)
1powerbank for powering the Raspberry Pi (any will do, just remember: the more mAh you have the longer you can keep it running)
1 Battery pack of 6 volts to run the servos
wires to connect everything
(http://www.robotshop.com/en/300mm-f-f-20-pin-jumper-wire-splittable.html)
and legos of course (or whatever you're making the chassis from)
Electronics and Soldering
The servos are controlled via PWM (Pulse Width Modulation) using the excellent Adafruit 16-channel PWM driver. Make sure to check out the tutorial on their website to understand it a little better and how to solder all the pins.

For the power we use a cheap 5 volts usb powerbank to power the raspberry pi and a cheap 7 volts lithium battery to power the servo's via the v+ pins.


The wiring goes as following:

the gnd pin on the servo controller goes to pin 6 ground on the rpi2
the scl pin on the servo controller goes to pin 3 scl 1 on the rpi2
the sda pin on the servo controller goes to pin 2 sda 1 on the rpi2
the vcc pin on the servo controller goes to pin 1 3v+ on the rpi2

The continuous rotation servo goes to contacts 0 of the servo controller and the 180 degrees servo goes to contacts 1.


Software
Finally, the Raspberry Pi must be loaded with some software which translates Xbox controller buttons into motor speed, motor direction, and steering rotation. 
The Xbox 360 Wireless Gaming Receiver for Windows is required to connect the controller. Microsoft use a custom wireless protocol, so a regular Bluetooth modem will not work. This bulky device consumes quite a lot of power, but at least it is relatively inexpensive.
“For Windows” should not be taken too seriously. Ingo Ruhnke’s excellent Xbox/Xbox 360 USB Gamepad Driver for Linux is a perfect solution for hooking up the wireless USB device, and it installs in seconds on a Raspberry Pi running Ubuntu.


# Right thumbstick controls the stearing
if event.key=='X2':
    steer = int( servoSteer + (servoSteerWidth*-event.value)/32768 )
    pwm.setPWM(1, 0, steer)
    
    
To run everything you must have a raspberry pi B or B+ with a fresh install of raspbian wheezy.

Make sure to update everything beforehand:
	sudo apt-get update
	sudo apt-get upgrade

make sure python is installed and updated and the interface libraries are:
	sudo apt-get install python-pip
	sudo easy_install -U distribute
	sudo apt-get install python-dev
	sudo pip install RPi.GPIO

Install the communications libraries:
sudo apt-get install python-smbus
	sudo apt-get install i2c-tools
	sudo modprobe i2c-bcm2708
	sudo modprobe i2c-dev

install the xbox driver
	sudo apt-get install xboxdrv

make sure it works
	sudo xboxdrv --wid 0 -l 2 --dpad-as-button --deadzone 12000
(if it doesn't work try to kill the xboxdrv task first)

make sure everything is connected at this point, the servo controller must be connected and powered on, the xbox module must be connected and the servos as well to their respective pins.

then finally execute the startup script to run everything:
	sudo ./lego-controller.sh


Building the Chassis
The design of the chassis aims to be as simple and robust as possible. Make sure it is as strong as possible, since the servos would tear the car apart if you don't build it as strong as you can.
If you are using lego, make sure you are using as much connector pins as you can and as much lego-technic as well. How you make it look is entirely up to you.


Notes
we encountered a problem that it wouldn't run and figured out we had to delete python 3 from the system, this only works in python 2!

To launch this on startup just add the file /lego-controller to the rc.local file (note: make sure to direct it to the file from the root folder, so if it is in your downloads folder: sudo /home/pi/Downloads/lego-pi-master/lego-controller.sh

If you start it up thru rc.local you have to kill the xboxdrv task first so add that command before lego-controller.sh.
