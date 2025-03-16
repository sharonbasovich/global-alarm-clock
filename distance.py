from machine import Pin, time_pulse_us
import time
import screen  # Assuming you have an LCD module like GpioLCD

# Define pins for the HC-SR04
trig_pin = Pin(15, Pin.OUT)  # Trigger pin (GPIO 15)
echo_pin = Pin(14, Pin.IN)   # Echo pin (GPIO 14)

# Function to measure distance
def measure_distance():
    # Send a 10us pulse to trigger the ultrasonic sensor
    trig_pin.value(0)
    time.sleep_us(2)
    trig_pin.value(1)
    time.sleep_us(10)
    trig_pin.value(0)
    
    # Measure the duration of the echo pulse
    pulse_duration = time_pulse_us(echo_pin, 1)
    
    # Calculate the distance (distance = pulse_duration / 2 / 29.1)
    # 29.1 is the speed of sound in cm/µs, divided by 2 because the pulse travels to the object and back
    distance = (pulse_duration / 2) / 29.1
    
    return distance

# Function to display the distance on the screen
def display_distance():
    # List to store the measured distances
    distances = []
    
    # Sample the distance five times
    for _ in range(5):
        distances.append(measure_distance())
    
    # Calculate the average distance
    average_distance = sum(distances) / len(distances)
    
    # Display the averaged distance
    screen.display_message(f"Distance: {average_distance:.2f} cm")
    
# Main loop to display distance
while True:
    display_distance()
    time.sleep(1)  # Update every second
