import time
from numpy import random
import multiprocessing
import RPi.GPIO as GPIO
from led8x8 import LED8x8

# define GPIO pins for data, latch, and clock
dataPins = 17
latchPins = 5
clockPins = 13

# init variables 
name = "led8x8"
xpos = 0
ypos = 0
boardState = multiprocessing.Array('i', 8)
boardState[xpos] = 1 << ypos
led = LED8x8(dataPins, latchPins, clockPins, name, boardState)

led.daemon = True
led.start()

try:
  while True:
    boardState[xpos] = 0
    xpos = xpos + random.randint(3) - 1
    ypos = ypos + random.randint(3) - 1
    if xpos < 0:
      xpos = 0
    elif xpos > 7:
      xpos = 7
    
    if ypos < 0:
      ypos = 0
    elif ypos > 7:
      ypos = 7
    boardState[xpos] = 1 << ypos
    time.sleep(0.1)
except KeyboardInterrupt:
  print('exiting random walk')
finally:
  led.terminate()