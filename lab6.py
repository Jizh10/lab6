import time
from numpy import random
import multiprocessing
import RPi.GPIO as GPIO
from led8x8 import LED8x8

dataPins = [17, 27]
latchPins = [5, 6]
clockPins = [13, 19]
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
    xpos = xpos + random.randint(2) - 1
    ypos = ypos + random.randint(2) - 1
    if xpos < 0:
      xpos = 7
    elif xpos > 7:
      xpos = 0
    
    if ypos < 0:
      ypos = 7
    elif ypos > 7:
      ypos = 0
    boardState[xpos] = 1 << ypos
    time.sleep(1)
except KeyboardInterrupt:
  print('exiting random walk')
finally:
  led.terminate()