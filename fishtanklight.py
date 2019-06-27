import RPi.GPIO as GPIO #Use GPIO library
import datetime #Use datetime library to get current time

GPIO.setwarnings(False)
ledPin = 11    # pin11 is connected to the led anode (+ve pin)
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(ledPin, GPIO.OUT)   # Set ledPin's mode as output
GPIO.output(ledPin, GPIO.HIGH) # Set ledPin high(+3.3V) to turn on led

while True: # Continue looping indefinitely
  now = datetime.datetime.now()    # Get the current time
  # Set time when to switch the light on
  timetoswitchon = datetime.datetime.now().replace(hour=12,minute=23,second=0,microsecond=0)
  # Set time when to switch the light off
  timetoswitchoff = datetime.datetime.now().replace(hour=12,minute=25,second=0,microsecond=0) 
  
  GPIO.output(ledPin, GPIO.LOW)    # light if off by default
  # Tuen lights on only when time is between timetoswitchon and timetoswitchoff
  if now >= timetoswitchon and now <= timetoswitchoff:
      GPIO.output(ledPin, GPIO.HIGH)
      
GPIO.cleanup(); #Clean up when exiting the program

