from machine import Pin, PWM
import time

# Define musical note frequencies (in Hz)
NOTE_C4  = 262
NOTE_C4S = 277  # C♯4 / D♭4
NOTE_D4  = 294
NOTE_D4S = 311  # D♯4 / E♭4
NOTE_E4  = 330
NOTE_F4  = 349
NOTE_F4S = 370  # F♯4 / G♭4
NOTE_G4  = 392
NOTE_G4S = 415  # G♯4 / A♭4
NOTE_A4  = 440
NOTE_A4S = 466  # A♯4 / B♭4
NOTE_B4  = 494

NOTE_C5  = 523
NOTE_C5S = 554  # C♯5 / D♭5
NOTE_D5  = 587
NOTE_D5S = 622  # D♯5 / E♭5
NOTE_E5  = 659
NOTE_F5  = 698
NOTE_F5S = 740  # F♯5 / G♭5
NOTE_G5  = 784
NOTE_G5S = 831  # G♯5 / A♭5
NOTE_A5  = 880
NOTE_A5S = 932  # A♯5 / B♭5
NOTE_B5  = 988

NOTE_C6  = 1047
NOTE_C6S = 1109  # C♯6 / D♭6
NOTE_D6  = 1175
NOTE_D6S = 1245  # D♯6 / E♭6
NOTE_E6  = 1319
NOTE_F6  = 1397
NOTE_F6S = 1480  # F♯6 / G♭6
NOTE_G6  = 1568
NOTE_G6S = 1661  # G♯6 / A♭6
NOTE_A6  = 1760
NOTE_A6S = 1865  # A♯6 / B♭6
NOTE_B6  = 1976

# Timing Constants for 120 BPM (4/4 time)
BPM = 180 #was 120 for rickroll
WHOLE = 60 / BPM * 4  # Whole note duration
HALF = WHOLE / 2
QUARTER = WHOLE / 4
EIGHTH = WHOLE / 8
SIXTEENTH = WHOLE / 16

buzzer1 = PWM(Pin(20))  # Use PWM on GPIO 16
buzzer2 = PWM(Pin(21))
# Define Megalovania melody: (frequency, duration)
megalovania_melody = [
    (NOTE_D4, 0.125), (NOTE_D4, 0.125), (NOTE_D5, 0.25), (NOTE_A4, 0.25), (0, 0.125), (NOTE_G4S, 0.25), (0, 0.125),
    (NOTE_G4, 0.125), (0, 0.125), (NOTE_F4, 0.25), (NOTE_D4, 0.125), (NOTE_F4, 0.125), (NOTE_G4, 0.125)
]

rickroll_melody = [
    (NOTE_C4, QUARTER + EIGHTH), (NOTE_D4, EIGHTH + HALF), (NOTE_D4, QUARTER), (NOTE_D4, EIGHTH),
    (NOTE_E4, EIGHTH + QUARTER), (NOTE_G4, SIXTEENTH), (NOTE_F4, SIXTEENTH), (NOTE_E4, SIXTEENTH),
    (NOTE_D4, SIXTEENTH), (NOTE_C4, QUARTER + EIGHTH), (NOTE_D4, EIGHTH + HALF), (NOTE_D4, QUARTER),
    (NOTE_C4, HALF + QUARTER)
]

jojo_melody = [
    (NOTE_F5S, QUARTER + EIGHTH), (NOTE_D5, HALF), (NOTE_D5, SIXTEENTH), (NOTE_E5, SIXTEENTH), (NOTE_F5, QUARTER),
    (NOTE_E5, QUARTER), (NOTE_D5, QUARTER), (NOTE_C5S, QUARTER), (NOTE_D5, QUARTER), (NOTE_E5, QUARTER),
    (NOTE_F5S, QUARTER + EIGHTH), (NOTE_B5, QUARTER + EIGHTH), (NOTE_B4, EIGHTH), (NOTE_C5S, EIGHTH),
    (NOTE_D5, QUARTER), (NOTE_E5, QUARTER), (NOTE_D5, QUARTER), (NOTE_C5S, QUARTER), (NOTE_A5, QUARTER),(NOTE_G5, QUARTER),
    (NOTE_F5S, QUARTER + EIGHTH), (NOTE_D5, HALF), (NOTE_D5, SIXTEENTH), (NOTE_E5, SIXTEENTH), (NOTE_F5, QUARTER),
    (NOTE_E5, QUARTER), (NOTE_D5, QUARTER), (NOTE_C5S, QUARTER), (NOTE_D5, QUARTER), (NOTE_E5, QUARTER),
    (NOTE_F5S, QUARTER + EIGHTH), (NOTE_B5, QUARTER + EIGHTH), (NOTE_B5, EIGHTH), (NOTE_C6S, EIGHTH), (NOTE_D6, QUARTER),
    (NOTE_G5, QUARTER), (NOTE_F5S, QUARTER), (NOTE_F5, QUARTER), (NOTE_D6, QUARTER), (NOTE_A5S, QUARTER), (NOTE_B4, HALF), (0, EIGHTH)
]

def play_tone(frequency, duration):
    """Plays a tone at the given frequency (Hz) for the specified duration (s)."""
    if frequency == 0:
        buzzer1.duty_u16(0)  # Rest (silence)
        buzzer2.duty_u16(0)  # Rest (silence)
    else:
        buzzer1.freq(frequency)
        buzzer1.duty_u16(30000)  # Adjust for volume
        buzzer2.freq(frequency)
        buzzer2.duty_u16(30000)  # Adjust for volume

    time.sleep(duration)  # Wait for note to play
    buzzer1.duty_u16(0)  #
    buzzer2.duty_u16(0)  # Turn off the buzzer
    time.sleep(0.05)  # Small pause between notes

# Play the Megalovania melody
while True:
    for note, length in megalovania_melody:
        play_tone(note, length)
