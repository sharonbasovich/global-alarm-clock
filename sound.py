from machine import Pin
import time

buzzer1 = Pin(19, Pin.OUT)  # Connect to a GPIO pin
buzzer2 = Pin(22, Pin.OUT)  # Connect to a GPIO pin

while True:
    buzzer1.value(1)  # Turn buzzer ON
    buzzer2.value(1) # Turn buzzer ON
    time.sleep(0.3)    # Wait 1 second
    buzzer1.value(0)  # Turn buzzer OFF
    buzzer2.value(0)  # Turn buzzer OFF
    time.sleep(0.3)    # Wait 1 second