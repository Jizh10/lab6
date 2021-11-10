import time
from led8x8 import LED8X8

dataPins = [17, 27]
latchPins = [5, 6]
clockPins = [13, 19]
name = "led8x8"

pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 
0b10100101, 0b10011001, 0b01000010, 0b00111100]

led = LED8X8(dataPins, latchPins, clockPins, name)

while True:
  led.diplay(pattern)
  time.sleep(0.4)

