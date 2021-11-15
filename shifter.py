# Shifter Class

import RPi.GPIO as GPIO
import time

class Shifter(object):

  def __init__(self, data, latch, clock):
    self.dataPin, self.latchPin, self.clockPin = data, latch, clock
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.dataPin, GPIO.OUT)
    GPIO.setup(self.latchPin, GPIO.OUT, initial=0)
    GPIO.setup(self.clockPin, GPIO.OUT, initial=0)

  def ping(self, pin): # ping the clock or latch pin
    GPIO.output(pin,1)
    time.sleep(0)
    GPIO.output(pin,0)
  
  def shiftByte(self, byteVal):
    for i in range(8):
      GPIO.output(self.dataPin, byteVal & (1<<i))
      self.ping(self.clockPin)
    self.ping(self.latchPin)
  
  def shiftByteNoLatch(self, byteVal):
    for i in range(8):
      GPIO.output(self.dataPin, byteVal & (1<<i))
      self.ping(self.clockPin)
  
  def pingLatch(self):
    GPIO.output(self.latchPin,1)
    time.sleep(0)
    GPIO.output(self.latchPin,0)
