import os 
import smtplib
from email.message import EmailMessage 
from email.utils import formataddr 
from pathlib import Path 

from dotenv import load_dotenv

PORT = 587
SMTP_SERVER = "smtp.gmail.com"

#load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

#read the environment variables
sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")


def send_email(receiver_emails, subject, name):
    message =  EmailMessage()
    message["Subject"] = subject
    message["From"] = formataddr(("Devina", f"{sender_email}"))
    message["To"] = ", ".join(receiver_emails)
    message.set_content(
        f"""\
Dear {name},
It's time for another NeetCode150 question!
Today's question is:
https://leetcode.com/problems/valid-parentheses/
Happy Coding!

        """
    )
    with smtplib.SMTP(SMTP_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_emails, message.as_string())
        print("Email sent successfully")
    
if __name__ == "__main__":
    send_email(
        subject="Test email",
        name = "Coder",
        receiver_emails=["db133@snu.edu.in", "ds192@snu.edu.in"]
    )
                   

