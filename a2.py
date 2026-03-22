import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_email =input( "your_email@gmail.com:")
receiver_email =input( "receiver_email@gmail.com:")
password =input( "your_app_password:")

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Python Attachment Email"

msg.attach(MIMEText("Sending attachment from Python", "plain"))

filename = "base.html"  # Change this to your file path

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename={filename}")

msg.attach(part)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)

server.send_message(msg)

print("✅ Email with attachment sent!")

server.quit()