import smtplib
import ssl
import os

def to_send(message):
    username='pschhabra22@gmail.com'

    password=os.getenv('PASSWORD')
    host='smtp.gmail.com'
    certifications=ssl.create_default_context()
    port='465'


    with smtplib.SMTP_SSL(host,port,context=certifications) as server:
        server.login(username,password)
        server.sendmail(username,username,message)