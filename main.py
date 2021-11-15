import time
import RPi.GPIO as GPIO
from led8x8 import LED8x8

dataPins = [17, 27]
latchPin = 5
clockPin = 13
name = "led8x8"

pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 
0b10100101, 0b10011001, 0b01000010, 0b00111100]


led = LED8x8(dataPins, latchPin, clockPin, name, pattern)

try:
  while True:
    led.display(pattern)
    time.sleep(0.001)
except KeyboardInterrupt:
  print('out')
finally:
  GPIO.cleanup()

