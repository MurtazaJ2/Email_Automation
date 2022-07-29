# Email_Automation

Step 1: Import modules.
Step 2: set up a connection to our email server.
 we’ll use smtp.starttls to enable transport layer security (TLS) encryption.
Step 3: built the message content.
Step 4: attach pictures and multiple attachments.
    First, read the image as binary data.
    Attach the image data to MIMEMultipart using MIMEImage, we add the given filename use os.basename.
Step 5: The last step is to send the email.
