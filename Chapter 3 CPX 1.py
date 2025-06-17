# Write your code here :-)
from adafruit_circuitplayground import cp
import time

while True:

    if cp.switch:
        cp.pixels[0] = (100, 100, 100)
    else:
        cp.pixels[0] = (0, 0, 0)

    if cp.button_a:
        cp.play_file("drum_cowbell.wav")

    if cp.button_b:
        cp.play_file("bass_hit_c.wav")

    if cp.touch_A1:
        cp.pixels[8] = (100, 100, 100)
    else:
        cp.pixels[8] = (0, 0, 0)
