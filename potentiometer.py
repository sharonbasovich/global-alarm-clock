from machine import Pin
import time
import screen  # Import the LCD module

# Rotary Encoder Pins
clk = Pin(18, Pin.IN, Pin.PULL_UP)
dt = Pin(17, Pin.IN, Pin.PULL_UP)
sw = Pin(16, Pin.IN, Pin.PULL_UP)

# Available options
options = ["A", "B", "C", "D"]
current_index = 0  # Tracks the selected option
last_state = clk.value()

def update_display():
    """Displays the current selection on the LCD."""
    screen.display_message(f"Option: {options[current_index]}")

def read_encoder():
    """Fixes direction detection for the rotary encoder."""
    global last_state, current_index
    current_state = clk.value()

    if (current_state != last_state) and (current_state == 1):  # Rotation detected
        time.sleep(0.001)  # Small debounce

        if dt.value() == current_state:  # Clockwise rotation
            current_index = (current_index + 1) % len(options)
        else:  # Counterclockwise rotation
            current_index = (current_index - 1) % len(options)

        update_display()  # Show updated option on LCD
        time.sleep(0.08)  # Extra delay to reduce sensitivity

    last_state = current_state


def read_button():
    """Confirms the selected option when the button is pressed."""
    if not sw.value():  # Button is active-low
        screen.display_message(f"Selected: {options[current_index]}")
        time.sleep(1)  # Show confirmation briefly
        update_display()  # Restore option display
