# sos.py: Blinks he SOS signal on the user LED: 3 short, 3 long, 2 short
# pulses followed by a 2s pause
# This is part of the course of small physics experiments at the
# African School of Fundamental Physics 2022
# Copyright (c) U.Raich
# The program is released under the MIT license

from machine import Pin
from time import sleep_ms
LED_PIN = 2

led = Pin(LED_PIN,Pin.OUT)
LONG_PULSE  = 700 # pulse length in ms
SHORT_PULSE = 200

def blink_once(delay):
    led.on()
    sleep_ms(delay)
    led.off()
    sleep_ms(delay)

while True:
    for i in range(3):
        blink_once(SHORT_PULSE)
    for i in range(3):
        blink_once(LONG_PULSE)
    for i in range(3):
        blink_once(SHORT_PULSE)
    sleep_ms(2000) # 2 s pause
