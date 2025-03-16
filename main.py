from potentiometer import read_encoder, read_button, update_display
from screen import display_message
import time

# display_message('test')
update_display()


# Main loop
while True:
    read_encoder()
    read_button()
    time.sleep(0.01)  # Small delay for stability