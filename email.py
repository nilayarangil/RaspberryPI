## Sending Email Alerts via Zoho
#
#
import smtplib

server = smtplib.SMTP_SSL('smtp.zoho.com',port=465) #server for sending the email

server.ehlo() # simple starting of the connection
server.login('nilayarangil@zoho.com','yourpwd') # login credentials and password

msg = """From:nilayarangil@zoho.com
Subject: Test Email \n
To: arunap@gmail.com \n
Message : This is an email send from raspberry pi \n"""
# This is where the email content goes. It could be information about the error, time of day, where in the script, etc.

server.sendmail('nilayarangil@zoho.com','arunap@gmail.com',msg) # this is where the email is sent to the recipient

server.quit() # exit the connection
print("email send")