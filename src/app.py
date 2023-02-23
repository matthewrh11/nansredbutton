from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os
import pyautogui
import subprocess
import datetime
import smtplib, ssl, time

def sendMail(send_email, rec_email, image_fp):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    img = open(image_fp, 'rb').read()

    message_text = """Hi {}! Nan is trying to do something on the computer and could really use your help, if you use the credentials in the attached picture, you can give her a hand! Let me know if you have any questions :)"""

    time_day = datetime.datetime.now()

    msg = MIMEMultipart()
    msg['Subject'] = 'Nan needs some help! ({}-{}-{} | {}:{})'.format(time_day.month, time_day.day, time_day.year, time_day.hour, time_day.minute)
    msg['From'] = send_email
    msg['To'] = rec_email

    text = MIMEText(message_text.format(email))
    msg.attach(text)
    image = MIMEImage(img, name=os.path.basename(image_fp))
    msg.attach(image)
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls() # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, email, msg.as_string())

    except Exception as e:
        print(e)
    finally:
        server.quit()

os.startfile(r'teamviewer/path')

time.sleep(10)

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r"Screen/Shot/Path")

sender_email = "sender_email@mail.com"
password = "password"

receiver_emails = [
    "family_member@mail.com"
]

for email in receiver_emails:
    sendMail(sender_email, email, r"Screen/Shot/Path")