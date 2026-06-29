# neopixel.py: Lights each LED of the ws2812 LED ring in red to find out which
# LED number corresponds to which physical LED
# Copyright U. Raich 2022
# The program is part of African School of Physics 2022

from machine import Pin
from neopixel import NeoPixel
from utime import sleep_ms

NEOPIXEL_PIN = 26
NO_OF_PIXELS = 7
# pixel mapping
pixelMap = [0,5,4,3,2,1,6]
neopixel = NeoPixel(Pin(NEOPIXEL_PIN),NO_OF_PIXELS)

red  = (31,0,0)
dark = (0,0,0)

for i in range(7):
    neopixel[pixelMap[i]] = red
    neopixel.write()
    sleep_ms(500)
    neopixel[pixelMap[i]] = dark
    sleep_ms(500)
    neopixel.write()

