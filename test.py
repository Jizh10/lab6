import time
from shifter import Shifter

dataPins = [17, 27]
latchPins = [5, 6]
clockPins = [13, 19]

rowShifter = Shifter(dataPins[0], latchPins[0], clockPins[0])
colShifter = Shifter(dataPins[1], latchPins[1], clockPins[1])

rowByteVal = 0b10000000
colByteVal = 0b00000000
while True:
  rowShifter.shiftByte(rowByteVal)
  colShifter.shiftByte(colByteVal)
  time.sleep(0.4)


