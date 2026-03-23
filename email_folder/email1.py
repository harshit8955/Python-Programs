import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = input("Enter your email: ")
password = input("Enter your password: ")   

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)

emails = {
    "user1@gmail.com": "Hello User 1!",
    "user2@gmail.com": "Hello User 2!",
    "user3@gmail.com": "Hello User 3!"
}

for email, message in emails.items():

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = "Personal Message"

    msg.attach(MIMEText(message, "plain"))

    server.sendmail(sender_email, email, msg.as_string())