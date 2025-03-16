from machine import Pin
import time

fan = Pin(28, Pin.OUT)  # Connect to a GPIO pin

def fanOn():
    fan.value(1);
    

def fanOff():
    fan.value(0);

while True:
    fanOn();
    time.sleep(1);    # Wait 1 second
    fanOff();
    time.sleep(1);

