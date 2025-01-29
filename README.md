<!-----



Conversion time: 0.961 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β40
* Wed Jan 29 2025 08:09:16 GMT-0800 (PST)
* Source doc: Untitled document
* This is a partial selection. Check to make sure intra-doc links work.
----->



# **Raspberry Pi 3 Projects with Various Sensors**

This Wiki page outlines four exciting and practical projects built using a **Raspberry Pi 3** and a variety of sensors. These projects integrate different capabilities, such as interacting with APIs, controlling home devices, sending emails, and creating a smart environment system. Let's dive into the details!


---


## **1. Interacting with ChatGPT API using Raspberry Pi**

This project demonstrates how to use the Raspberry Pi 3 to interact with the **ChatGPT API**. It can be used for creating interactive chatbots, personal assistants, or even home automation systems that respond to natural language inputs.


### **Components Needed:**



* Raspberry Pi 3 (any model with internet connectivity)
* Python 3.x
* OpenAI ChatGPT API key
* Internet connection (Wi-Fi or Ethernet)
* External microphone and speaker (optional for voice interaction)


### **Steps:**



1. **Install Required Packages:**
    * Install `requests` to interact with the ChatGPT API.
    * You may also use libraries like `speech_recognition` and `pyttsx3` to convert speech to text and text to speech.

bash \
CopyEdit \
`sudo apt-get install python3-pip`


```
pip3 install requests speechrecognition pyttsx3

```



2. 
3. **Obtain API Key:**
    * Sign up for an OpenAI account and get your ChatGPT API key from[ OpenAI](https://beta.openai.com/signup/).
4. **Write Python Script:**
    * Create a Python script that sends a request to the ChatGPT API using the user's text input (or voice input, if you use speech recognition).
    * Send the text to the API and fetch the response.

Example: \
python \
CopyEdit \
`import requests`


```
api_key = 'your-openai-api-key'
endpoint = "https://api.openai.com/v1/chat/completions"

def chatgpt_query(message):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}]
    }
    response = requests.post(endpoint, json=data, headers=headers)
    return response.json()['choices'][0]['message']['content']

while True:
    user_input = input("Ask me something: ")
    response = chatgpt_query(user_input)
    print("ChatGPT Response: ", response)

```



5. 


### **Applications:**



* Create voice-enabled ChatGPT assistants for home automation.
* Integrate ChatGPT into smart devices like a smart speaker system.


---


## **2. Controlling Fish Tank Light with Raspberry Pi**

This project involves controlling a fish tank light based on various factors like time of day or environmental conditions. The Raspberry Pi interacts with a relay switch to control the light.


### **Components Needed:**



* Raspberry Pi 3
* Relay Module
* Fish tank light
* Jumper wires
* Python 3.x


### **Steps:**



1. **Wiring the Relay:**
    * Connect the relay module to the Raspberry Pi GPIO pins. Ensure the fish tank light is connected to the relay to allow it to be controlled.
2. **Install Required Libraries:**
    * Install the `RPi.GPIO` library to control the GPIO pins.

bash \
CopyEdit \
`sudo apt-get install python3-rpi.gpio`



3. 
4. **Python Script for Control:**
    * Write a Python script to control the relay based on the time of day or other triggers (e.g., ambient light).

Example: \
python \
CopyEdit \
`import RPi.GPIO as GPIO`


```
import time
from datetime import datetime

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Assume relay is connected to GPIO 17

def control_light():
    current_hour = datetime.now().hour
    if 6 <= current_hour < 18:
        GPIO.output(17, GPIO.HIGH)  # Turn light ON during daytime
    else:
        GPIO.output(17, GPIO.LOW)  # Turn light OFF during nighttime

while True:
    control_light()
    time.sleep(60)  # Check every minute

```



5. 


### **Applications:**



* Automated fish tank lighting system.
* Can be modified to control other appliances based on time of day or environment.


---


## **3. Sending Emails using Zoho SMTP with Raspberry Pi**

This project demonstrates how the Raspberry Pi can send emails using **Zoho SMTP** server, which can be useful for automation tasks, notifications, or alerts.


### **Components Needed:**



* Raspberry Pi 3
* Python 3.x
* SMTP credentials (Zoho email)


### **Steps:**



1. **Install Required Libraries:**
    * Install `smtplib` (comes pre-installed with Python) for sending emails via SMTP.
2. **Setup Zoho SMTP:**
    * Sign up for a Zoho Mail account if you don't have one and enable SMTP access.
3. **Python Script to Send Email:**
    * Write a Python script that sends an email using Zoho's SMTP server.

Example: \
python \
CopyEdit \
`import smtplib`


```
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "your-email@zoho.com"
receiver_email = "recipient-email@example.com"
password = "your-zoho-email-password"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Test Email from Raspberry Pi"

body = "This is a test email sent using Zoho SMTP and Raspberry Pi!"
msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP('smtp.zoho.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()

```



4. 


### **Applications:**



* Send automated notifications for various events (e.g., system alerts, sensor data thresholds).
* Integrate email notifications into other Raspberry Pi projects.


---


## **4. Smart Humidifier Control System**

This project demonstrates how to create a **smart humidifier** that controls the room's humidity by turning the humidifier on or off based on the humidity level detected by a sensor.


### **Components Needed:**



* Raspberry Pi 3
* DHT22 or DHT11 Humidity Sensor
* Relay Module (to control the humidifier)
* Humidifier
* Python 3.x


### **Steps:**



1. **Connect the Humidity Sensor:**
    * Connect the DHT22 or DHT11 sensor to the Raspberry Pi GPIO pins.
2. **Install Required Libraries:**
    * Install the necessary libraries for reading data from the DHT sensor.

bash \
CopyEdit \
`sudo pip3 install Adafruit_DHT`



3. 
4. **Write Python Script:**
    * Write a Python script to read the humidity level from the sensor and turn the humidifier on/off based on the threshold.

Example: \
python \
CopyEdit \
`import Adafruit_DHT`


```
import RPi.GPIO as GPIO
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO Pin connected to DHT22
RELAY_PIN = 17  # GPIO Pin connected to relay

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Desired humidity threshold
desired_humidity = 60

def control_humidifier():
    humidity, _ = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None:
        if humidity < desired_humidity:
            GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn on the humidifier
            print(f"Humidity low ({humidity}%), turning on humidifier.")
        else:
            GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn off the humidifier
            print(f"Humidity normal ({humidity}%), turning off humidifier.")
    else:
        print("Failed to retrieve humidity data.")

while True:
    control_humidifier()
    time.sleep(60)  # Check humidity every minute

```



5. 


### **Applications:**



* Automated humidifier control based on room conditions.
* Smart home automation for air quality management.


---


## **Conclusion**

These projects demonstrate the versatility of the **Raspberry Pi 3** and how it can be used to interact with various sensors and devices to create practical, smart systems. Whether you’re building an intelligent chatbot, controlling home appliances, sending emails, or managing environmental conditions, the Raspberry Pi offers a great platform for experimentation and learning.
