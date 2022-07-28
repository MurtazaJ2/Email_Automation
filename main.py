import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os


def send_email(receiver_email, text):
    sender_email = 'abc@softnautics.com'
    receiver_email = receiver_email
    password = "rkqjvpmhvnrhmb"

    connection = smtplib.SMTP("smtp-mail.outlook.com", 587)
    connection.starttls()
    connection.login(user=sender_email, password=password)
    connection.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=text.as_string())
    connection.quit()


def message(receiver_email, subject, text="", img=None, attachment=None):
    message = MIMEMultipart()
    message['Subject'] = subject
    message.attach(MIMEText(text))

    if img is not None:
        if type(img) is not list:
            img = [img]

        for one_img in img:
            img_data = open(one_img, 'rb').read()
            message.attach(MIMEImage(img_data, name=os.path.basename(one_img)))

    if attachment is not None:
        if type(attachment) is not list:
            attachment = [attachment]

        for one_attachment in attachment:
            with open(one_attachment, 'rb') as f:
                file = MIMEApplication(f.read(), name=os.path.basename(one_attachment))
            file['Content-Disposition'] = f'attachment; filename="{os.path.basename(one_attachment)}"'
            message.attach(file)
    send_email(receiver_email, message)


msg = """
hey bhargav!!
    this mail is test email from python, with multiple attachments. 
    would love to hear comments from your side
    
    
thank you!
"""
subject = "mail with multiple attachments"

message('xyz@softnautics.com', subject, text=msg,
        img='/home/murtaza/Pictures/Screenshot from 2022-05-27 09-41-26.png',
        attachment='/home/murtaza/Documents/try1.txt')
