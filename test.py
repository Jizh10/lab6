import time
from shifter import Shifter
import RPi.GPIO as GPIO

dataPin = 17
latchPin = 5
clockPin = 13

shifter = Shifter(dataPin, latchPin, clockPin)


rowByteVal = 0b10000000
colByteVal = 0b01111111
byteVal = rowByteVal

for i in range(8):
  if colByteVal & (1<<(7-i)):
    byteVal = (byteVal << 1) + 1
  else:
    byteVal = byteVal << 1

print(bin(byteVal))

pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 
0b10100101, 0b10011001, 0b01000010, 0b00111100]

try:  
  while True:
    shifter.shiftDoubleByte(byteVal)
    time.sleep(0.4)
except KeyboardInterrupt:
  print('out')
finally:
  GPIO.cleanup()

