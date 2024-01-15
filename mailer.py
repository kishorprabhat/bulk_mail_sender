import smtplib
import ssl
from email.message import EmailMessage
import time
import yaml
import csv

# Loading the YAML configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)


smtp_server = config["smtp"]["server"]
smtp_port = config["smtp"]["port"]
smtp_username = config["smtp"]["username"]
smtp_password = config["smtp"]["password"]
ca_certificate = config["smtp"]["certs"]

# List of recipient email addresses
recipients = config["email"]["list"]

# Email content
subject = config["email"]["subject"]
body = """
Hey there,

Hope you are doing well . Recently I came across an opening in your company name for Senior Java Backend Engineer.
It would be great if you could provide me a referral for the same. 
Why me? 
    -> 5.5+ year of Experience in Java , SpringBoot, Microservices. 
    -> Worked in Banking Domain I have attached my resume for the same.

Hope to hear from you soon. Thanks
"""

# Attachment
attachmentpath = config["email"]["attachment"]["path"]
attachmentname = config["email"]["attachment"]["name"]
sendattachment = config["email"]["attachment"]["send"]
# Create a secure SSL context for secure communication
context = ssl.create_default_context(cafile=ca_certificate)

# Function to handle potential errors and delays
def send_email(recipient):
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(smtp_username, smtp_password)
            message = EmailMessage()
            message["From"] = smtp_username
            message["To"] = recipient
            message["Subject"] = subject
            message.set_content(body)

            if ( sendattachment == True):
                # Attach a file
                with open(attachmentpath + attachmentname, "rb") as attachment:
                    file_data = attachment.read()
                    file_type = "application/pdf"  # Adjust based on file type
                    file_name = attachmentname
                    message.add_attachment(file_data, maintype=file_type, subtype="pdf", filename=file_name)


            server.send_message(message)
            print(f"Email sent to: {recipient}")
    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")
        # Optionally retry after a delay
        time.sleep(60)  # Wait for 1 minute before retrying

# # Send emails to each recipient
# for recipient in recipients:
#     send_email(recipient)

# Read recipients from CSV
with open(recipients, "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    recipients = list(reader)
    email_addresses = [row[0] for row in recipients]

# Send emails to each recipient
for email_address in email_addresses:
    send_email(email_address)  # Call your send_email function