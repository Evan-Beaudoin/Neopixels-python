#Created By: Evan

#Created on: Sept. 2020

#This program: Uses neopixels for traffic lights loop

from microbit import *
import neopixel
from random import randint

np = neopixel.NeoPixel(pin16, 4)

while True:
    np[3] = (0, 255, 0)
    np.show()
    sleep(1000)
    np.clear()
    np[2] = (255, 255, 0)
    np.show()
    sleep(1000)
    np.clear()
    np[1] = (255, 0, 0)
