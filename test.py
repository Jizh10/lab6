import time
from shifter import Shifter
import RPi.GPIO as GPIO

dataPins = [17, 27]
latchPin = 5
clockPin = 13

rowShifter = Shifter(dataPins[0], latchPin, clockPin)
colShifter = Shifter(dataPins[1], latchPin, clockPin)

rowByteVal = 0b10000000
colByteVal = 0b01111111

pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 
0b10100101, 0b10011001, 0b01000010, 0b00111100]

try:  
  while True:
    rowShifter.shiftByte(rowByteVal)
    colShifter.shiftByte(colByteVal)
    time.sleep(0.4)
except KeyboardInterrupt:
  print('out')
finally:
  GPIO.cleanup()

