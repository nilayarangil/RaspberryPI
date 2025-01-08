import RPi.GPIO as GPIO
import time
import datetime

def WriteToFile(fname,data):
    f = open(fname, "a")
    f.write(data + "\r\n")  
    f.close()

while True:
    #Set pin 17 to send data to relay switch
    pin = 17

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    def PlugOn(pin):
        GPIO.output(pin, GPIO.LOW)

    def PlugOff(pin):
        GPIO.output(pin, GPIO.HIGH)

    h,t = dht.read_retry(dht.DHT22, 4)  

    far = (t * 9/5) + 32 

    if h is not None and t is not None:
        now = datetime.datetime.now()
        hr = datetime.datetime.now().hour
        
        
        #print("Temp=",int(far),"F","Humidity=",int(h),"%"," at ",now.strftime("%H:%M:%S"))
        
        #write humidity and temp to a file
        WriteToFile("humidity.txt",str(datetime.datetime.now()) + "," + str(h))
        WriteToFile("temperture.txt",str(datetime.datetime.now()) + "," + str(far))
      
        PlugOff(pin) 

        if int(h) < 53:
            #write to file when humidifier was switched on
            WriteToFile("records.txt","Switched on at " + str(datetime.datetime.now()) + " when humidity was " + str(h))
            #Turn on humidifier
            PlugOn(pin)
            #take next reading in 5 mins

        time.sleep(60)
    else:
        WriteToFile("records.txt","error starting program")

