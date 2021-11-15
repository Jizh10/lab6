import time
from shifter import Shifter
import RPi.GPIO as GPIO

dataPins = [17, 27]
latchPin = 5
clockPins = [13, 19]

rowShifter = Shifter(dataPins[0], latchPin, clockPins[0])
colShifter = Shifter(dataPins[1], latchPin, clockPins[1])

rowByteVal = 0b10000000
colByteVal = 0b01111111

pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 
0b10100101, 0b10011001, 0b01000010, 0b00111100]

try:  
  while True:
    rowShifter.shiftByteNoLatch(rowByteVal)
    colShifter.shiftByteNoLatch(colByteVal)
    rowShifter.pingLatch()
    time.sleep(0.4)
except KeyboardInterrupt:
  print('out')
finally:
  GPIO.cleanup()

