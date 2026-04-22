# ASP2026
Course material for the **A**frican **S**chool of **P**hysics 2026, Nairobi, Kenya
## Introduction
At ASP2022 a workshop on small physics experiments and the **I**nternet **o**f **T**hings (IoT) has been integrated for the first time. This is a hands-on workshop where the students create small experiments.
While in 2022 only simulated senors (a push button switch for digital sensors and a linear potentiometer for analogues sensors) have been used, the 2024 edition has been extended to real electronic sensors (temperature, humidity, barometric pressure) and actuators (Leds, TFT display, stepping motors). The sensors are read and the actuators are controlled with simple Python programs. 
The laboratory equipment consists of
* an ESP32 CPU card with a MicroPython interpreter installed in its flash memory
  a user programmable LED connected to a **G**eneral **P**urpose **I**nput **O**utput (GPIO) line on the CPU card
* a USB C (or micro USB) cable for flash programming of uploading the users MicroPython programs
* a 3 slot backplane connecting the CPU to the sensors and actuators
* a pushbuttom switch connected to a GPIO line via the backplane
* a 10 k&Omega; linear potentiometer connected to the **A**nalogue to **D**igital **C**onverter (ADC) on the ESP32 chip
* a 7 LED NeoPixel ring
* a SHT30 air temperature and relative humidity sensor
* a BMP180 barometric pressure sensor
* a 128x64 pixel **O**rganic **LED** (OLED) display
* a stepping motor with driver   

Most is the information comes from the ASP2024 school in Marrakesh but it has been extended and upgraded for ASP2026 in Nairobi. In particular a new chapter on ESPNOW was been added.
Please check the Wiki pages for more information.
This is work in progress.
