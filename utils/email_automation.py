import smtplib
import os
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'opticoptimizers@gmail.com'
SMTP_PASSWORD = 'yqyk iwfh cayg jgbk'
EMAIL_FROM = 'opticoptimizers@gmail.com'


EMAIL_TO = '9921004497@klu.ac.in'

def mailer(EMAIL_TO,name):
    global EMAIL_FROM
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = 'KARE-OSS FACEIT VERSION 1 !'
    text = MIMEText(f"Dear {name},\n\nYour attendance has been recorded Successfully.\n\nThanks & Regards,\nKARE-OSS Team")
    msg.attach(text)
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())


df = pd.read_csv('attendance/output.csv')
emails,names,in_time,out_time,total,regno = df['Email'].tolist(),df['Name'].tolist(),df['InTime'].tolist(),df['OutTime'].tolist(),df['TimeDifference'].tolist(),df['Roll No'].tolist()

for i in range(len(emails)):
    mailer(emails[i],names[i])
    print(f"Mail sent to {names[i]}")
