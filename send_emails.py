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

def send_email(receiver_email, subject, name):
    message =  EmailMessage()
    message["Subject"] = subject
    message["From"] = formataddr(("Devina", f"{sender_email}"))
    message["To"] = receiver_email
    message.set_content(
        f"""\
        Dear {name},
        hope this email finds you well.
        warm regards, 
        devina
        """
    )
    with smtplib.SMTP(SMTP_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    
    if __name__ == "__main__":
        send_email(
            subject="Test email",
            name = "devina",
            receiver_email="db133@snu.edu.in"
        )
                   

