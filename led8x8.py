# LED 8x8 class
import time
import multiprocessing
from shifter import Shifter

class LED8x8(multiprocessing.Process):

  def __init__(self, data, latch, clock, process_name):
    multiprocessing.Process.__init__(self, name=process_name)
    self.rowShifter = Shifter(data[0], latch[0], clock[0])
    self.colShifter = Shifter(data[1], latch[1], clock[1])

  def run(self, pattern):
    print("Process started")
    self.display(pattern)
    print("Process ended")

  def display(self, pattern):
    for i in range(8):
      self.rowShifter.shiftByte(1<<(7-i)) 
      self.colShifter.shiftByte(~(pattern[i]))
      time.sleep(0.002)
      
    