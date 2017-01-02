# Lego-pi<br>
My version of the lego pi car from Tom Rees, uses two servos instead of one servo and a different motor. All credit goes to him!<br>
<br>
HOW TO: Build an RC Car using Lego and a Raspberry Pi<br>
Parts list (I bought everything from a local shop, this is just for reference, I only ordered the Adafruit driver from the Adafruit website)<br>
The parts at least necessary for this project are as following:<br>
1Raspberry pi B/B+ (you can find them all over)<br>
1Adafruit 16-Channel 12-bit PWM/Servo Driver - I2C interface - PCA9685 (this is the servo controller)<br>
1 Servo motor for driving (http://www.robotshop.com/en/hitec-hs422-servo-motor.html) <br>
1 Servo motor for steering (http://www.robotshop.com/en/gws-naro-servo-motor.html)<br>
1powerbank for powering the Raspberry Pi (any will do, just remember: the more mAh you have the longer you can keep it running)<br>
1 Battery pack of 6 volts to run the servos<br>
wires to connect everything<br>
(http://www.robotshop.com/en/300mm-f-f-20-pin-jumper-wire-splittable.html)<br>
and legos of course (or whatever you're making the chassis from)<br>
<br>
Electronics and Soldering<br>
The servos are controlled via PWM (Pulse Width Modulation) using the excellent Adafruit 16-channel PWM driver. Make sure to check out the tutorial on their website to understand it a little better and how to solder all the pins.<br>
<br>
For the power we use a cheap 5 volts usb powerbank to power the raspberry pi and a cheap 7 volts lithium battery to power the servo's via the v+ pins.<br>
<br>
<br>
The wiring goes as following:
<br>
the gnd pin on the servo controller goes to pin 6 ground on the rpi2<br>
the scl pin on the servo controller goes to pin 3 scl 1 on the rpi2<br>
the sda pin on the servo controller goes to pin 2 sda 1 on the rpi2<br>
the vcc pin on the servo controller goes to pin 1 3v+ on the rpi2<br>
<br>
The continuous rotation servo goes to contacts 0 of the servo controller and the 180 degrees servo goes to contacts 1.<br>
<br>
<br>
Software<br>
Finally, the Raspberry Pi must be loaded with some software which translates Xbox controller buttons into motor speed, motor direction, and steering rotation. <br>
The Xbox 360 Wireless Gaming Receiver for Windows is required to connect the controller. Microsoft use a custom wireless protocol, so a regular Bluetooth modem will not work. This bulky device consumes quite a lot of power, but at least it is relatively inexpensive.
“For Windows” should not be taken too seriously. Ingo Ruhnke’s excellent Xbox/Xbox 360 USB Gamepad Driver for Linux is a perfect solution for hooking up the wireless USB device, and it installs in seconds on a Raspberry Pi running Ubuntu.<br>
<br>
<br>
# Right thumbstick controls the stearing<br>
if event.key=='X2':<br>
    steer = int( servoSteer + (servoSteerWidth*-event.value)/32768 )<br>
    pwm.setPWM(1, 0, steer)<br> 
<br>  
To run everything you must have a raspberry pi B or B+ with a fresh install of raspbian wheezy.
<br>
Make sure to update everything beforehand:<br>
	sudo apt-get update<br>
	sudo apt-get upgrade<br>
<br>
make sure python is installed and updated and the interface libraries are:<br>
	sudo apt-get install python-pip<br>
	sudo easy_install -U distribute<br>
	sudo apt-get install python-dev<br>
	sudo pip install RPi.GPIO<br>
<br>
Install the communications libraries:<br>
	sudo apt-get install python-smbus<br>
	sudo apt-get install i2c-tools<br>
	sudo modprobe i2c-bcm2708<br>
	sudo modprobe i2c-dev<br>
<br>
install the xbox driver<br>
	sudo apt-get install xboxdrv<br>
<br>
make sure it works<br>
	sudo xboxdrv --wid 0 -l 2 --dpad-as-button --deadzone 12000<br>
(if it doesn't work try to kill the xboxdrv task first)<br>
<br>
make sure everything is connected at this point, the servo controller must be connected and powered on, the xbox module must be connected and the servos as well to their respective pins.<br>
<br>
then finally execute the startup script to run everything:<br>
	sudo ./lego-controller.sh<br>
<br>
<br>
Building the Chassis<br>
The design of the chassis aims to be as simple and robust as possible. Make sure it is as strong as possible, since the servos would tear the car apart if you don't build it as strong as you can.<br>
If you are using lego, make sure you are using as much connector pins as you can and as much lego-technic as well. How you make it look is entirely up to you.<br>
<br>
<br>
Notes<br>
we encountered a problem that it wouldn't run and figured out we had to delete python 3 from the system, this only works in python 2!<br>
<br>
To launch this on startup just add the file /lego-controller to the rc.local file (note: make sure to direct it to the file from the root folder, so if it is in your downloads folder: sudo /home/pi/Downloads/lego-pi-master/lego-controller.sh<br>
<br>
If you start it up thru rc.local you have to kill the xboxdrv task first so add that command before lego-controller.sh.<br>
<br>
If you get the following error or something like it:<br>
Traceback (most recent call last):
  <br>File "/home/pi/Lego-pi/control.py", line 4, in <module>
    from lib.Adafruit_PWM_Servo_Driver import PWM<br>
  File "/home/pi/Lego-pi/lib/Adafruit_PWM_Servo_Driver.py", line 5, in <module>
    from Adafruit_I2C import Adafruit_I2C<br>
  File "/home/pi/Lego-pi/lib/Adafruit_I2C.py", line 9, in <module>
    class Adafruit_I2C :<br>
  File "/home/pi/Lego-pi/lib/Adafruit_I2C.py", line 11, in Adafruit_I2C
    def __init__(self, address, bus=smbus.SMBus(0), debug=False):<br>
IOError: [Errno 2] No such file or directory<br>
xboxdrv: no process found<br>
 change <br>
 def __init__(self, address, bus=smbus.SMBus(0), debug=False): <br>
 to <br>
 def __init__(self, address, bus=smbus.SMBus(1), debug=False):<br>
 or the other way around for the RPi A or B<br>
