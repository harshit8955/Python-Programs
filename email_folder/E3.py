import smtplib

# Sender and receiver email
sender_email = "harshitgunjan8020@gmail.com"
receiver_email = "harshitffid8020@gmai.com"

# Gmail App Password (NOT your normal Gmail password)
password = "kbra ywvn zzsk lxzt"    #we have to put app password here instead of normal password because google does not allow to use normal password for security reasons. So we have to generate app password from our google account and use that app password here.

# Email message
message = """Subject: Test Email

Hello,
This is a basic email sent using Python.
"""

# Connect to Gmail server
server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

# Login
server.login(sender_email, password)

# Send email
server.sendmail(sender_email, receiver_email, message)

print("✅ Email sent successfully!")

# Close connection
server.quit()