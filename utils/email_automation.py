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
    msg['Subject'] = 'KARE-OSS FACEIT TEST !'
    text = MIMEText(f"Dear {name},\n\nWe would like to express our sincere gratitude for your participation in the KARE OSS Kaggle Code Competition held on 19th June. Your contribution and dedication were instrumental in making the competition a resounding success. We were impressed by your exceptional skills and problem-solving abilities, which truly elevated the standard of the event. Thank you for showcasing the spirit of collaboration and innovation.\n\nAs a token of appreciation, we have attached a participation certificate to this email. It serves as a memento of your outstanding performance and demonstrates our recognition of your hard work. We hope you cherish this certificate as a testament to your remarkable skills.\n\nThe success of this competition has inspired us to organize more such events in the future. We eagerly await the opportunity to see you participate in our upcoming events.\n\nBest regards,\nN V ANAND SAI (PRESIDENT,OSS),\nB KUMAR SRINIVAS (VICE-PRESIDENT,OSS),\nB KARTHIK TARAKA SAI (SECRETARY,OSS),\n& TEAM KARE-OSS.")
    msg.attach(text)
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())


df = pd.read_csv('attendance/output.csv')
print(df)
