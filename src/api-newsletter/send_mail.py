from dotenv import load_dotenv
from email.message import EmailMessage
from email.mime.text import MIMEText
import json
import os
import smtplib


load_dotenv()


def send_mail(
    recipient: str,
    subject: str = "Newsletter",
    body: str = "<h1>Hi</h1><br /><p>Wow this is a newsletter</p>",
):
    EMAIL_ADDR = os.environ["EMAIL_ADDR"]
    EMAIL_PASS = os.environ["EMAIL_PASS"]

    email_message = EmailMessage()

    email_message["From"] = EMAIL_ADDR
    email_message["To"] = recipient
    email_message["Subject"] = subject

    email_message.set_content(body, subtype="html")

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp_client:
        smtp_client.ehlo()
        smtp_client.starttls()
        smtp_client.ehlo()
        smtp_client.login(EMAIL_ADDR, EMAIL_PASS)
        smtp_client.send_message(email_message)
