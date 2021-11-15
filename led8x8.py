# LED 8x8 class
import time
import multiprocessing
from shifter import Shifter

class LED8x8(multiprocessing.Process):

  def __init__(self, data, latch, clock, process_name, pattern):
    multiprocessing.Process.__init__(self, name=process_name)
    self.pattern = pattern
    self.shifter = Shifter(data, latch, clock)

  def run(self):
    print("Process started")
    try:
      while True:
        self.display(self.pattern)
    except KeyboardInterrupt:
      print('exiting process')
    finally:  
      print("Process ended")

  def display(self, pattern):
    for i in range(8):
      byteVal = 1<<(7-i)
      for j in range(8):
        if pattern[i] & (1<<(7-j)):
          byteVal = byteVal<<1
        else:
          byteVal = (byteVal<<1)+1
      self.shifter.shiftDoubleByte(byteVal) 
      time.sleep(0.001)
      
    