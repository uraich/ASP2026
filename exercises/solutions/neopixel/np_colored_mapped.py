# neopixel.py: Lights each LED of the ws2812 LED ring with colors ranging from
# blue to red and white. The LEDs are lit sequentially.
# Copyright U. Raich 2022
# The program is part of African School of Physics 2022

from machine import Pin
from neopixel import NeoPixel
from utime import sleep_ms

NEOPIXEL_PIN = 26
neopixel = NeoPixel(Pin(NEOPIXEL_PIN),7)

# pixel mapping
pixelMap = [0,5,4,3,2,1,6]

colors = [(0x00, 0x00, 0x1f), # blue
          (0x00, 0x1f, 0x1f), # cyan
          (0x00, 0x1f, 0x00), # green
          (0x1f, 0x1f, 0x00), # yellow
          (0x1f, 0x00, 0x1f), # magenta
          (0x1f, 0x00, 0x00), # red
          (0x1f, 0x1f, 0x1f)] # white#] # 
dark = (0,0,0)

for i in range(0,6):
    neopixel[pixelMap[i]] = colors[i]
    neopixel.write()
    sleep_ms(1000)
    neopixel[pixelMap[i]] = dark
    sleep_ms(200)

neopixel[6] = colors[6]
neopixel.write()
sleep_ms(1000)
neopixel[6] = dark
neopixel.write()
