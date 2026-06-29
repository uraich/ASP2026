# adc2led.py:  The program  reads the ADC and selects an LED to light,
#              depending on the ADC value
# 
# Copyright U. Raich 2026
# The program is part of African School of Physics 2026
# Released under the MIT license

import sys
from utime import sleep_ms
from machine import Pin,ADC
from neopixel import NeoPixel

# We set the max LED intensity to 31 in order not to blind our eyes
MAX_INTENSITY = 31
NEOPIXEL_PIN = 26
NO_OF_LEDS   = 7
DIVIDER = 4096 // 7 + 1 # make sure the values stay between 1 and 7

dark = (0,0,0)
# pixel mapping
# use the below mapping table with the LED ring on the prototype board
# otherwise: pixelMap = [0,1,2,3,4,5,6]
pixelMap = [0,5,4,3,2,1,6]

# init the NeoPixel driver
neopixel = NeoPixel(Pin(NEOPIXEL_PIN),NO_OF_LEDS)

# init the linear potentiometer
slider = ADC(Pin(36),atten=ADC.ATTN_11DB)  # create ADC object on ADC pin 36

old_led = 0

# clear all LEDs
def clearLEDs():
    for i in range(NO_OF_LEDS):
        neopixel[i] = dark
    neopixel.write()

def showLED(led):
    neopixel[pixelMap[led]] = (0,0,MAX_INTENSITY) # set the LED to blue
    neopixel.write()
    
clearLEDs()
print("Divider: ",DIVIDER)
while True:
    try:
        # read the ADC
        led = slider.read() // DIVIDER  # get the LED that needs lighting
        if led != old_led:
            clearLEDs()
            old_led = led
            print("Leds to be lit: ",led)
            showLED(led)
        sleep_ms(100)
    except KeyboardInterrupt:
        clearLEDs()
        break;
            
