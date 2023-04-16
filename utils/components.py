from gpiozero import Button, Servo
from gpiozero.pins.pigpio import PiGPIOFactory

from time import sleep
import threading

pigpio_factory = PiGPIOFactory()

push_to_talk_button = Button(4)
mouth_servo = Servo(26, pin_factory=pigpio_factory)

move_mouth = False

def _move_servo(servo):
    while move_mouth:
        servo.min()
        sleep(0.3)
        servo.max()
        sleep(0.3)
    
    servo.min() # Move back to default position

def move_mouth_servo():
    global move_mouth 
    move_mouth = True

    servo_thread = threading.Thread(target=_move_servo, args=(mouth_servo,))
    servo_thread.start()

def stop_mouth_servo():
    global move_mouth 
    move_mouth = False