import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = input("your_email@gmail.com:")
receiver_email = input("receiver_email@gmail.com:")
app_password = input("your_16_digit_app_password:")

# Create message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email from Python"

body = "Hello Harshit,\n\nThis email is sent using Python successfully 🚀"

message.attach(MIMEText(body, "plain"))

# Connect to Gmail server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Login
server.login(sender_email, app_password)

# Send email
server.send_message(message)

print("✅ Email sent successfully!")

# Close server
server.quit()

