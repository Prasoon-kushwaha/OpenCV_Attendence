import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(body, to_email,subject="Attendance is Accepted"):
    sender_email = "attendance.system.iiitu@gmail.com"
    sender_password = "ybuvdmuobsaarrzq"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())

if __name__ == "__main__":
    subject = "Attendance is Accepted"
    body = "Dear recipient, your attendance is accepted. Thank you!"
    to_email = "22146@iiitu.ac.in"
    send_email(subject, body, to_email)
