import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os
import ssl
from typing import List, Optional

def send_email(receiver_email: str, email_content: MIMEMultipart) -> None:
    """
    Send an email to the specified receiver.

    Args:
    receiver_email (str): The email address of the receiver.
    email_content (MIMEMultipart): The email content.
    """
    sender_email = os.environ.get("SENDER_EMAIL")
    password = os.environ.get("PASSWORD")

    if sender_email is None or password is None:
        raise ValueError("Sender email and password must be set")

    context = ssl.create_default_context()
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        try:
            server.sendmail(sender_email, receiver_email, email_content.as_string())
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")
        else:
            print("Email sent successfully")


def create_email(
    subject: str,
    text: str = "",
    images: Optional[List[str]] = None,
    attachments: Optional[List[str]] = None,
) -> MIMEMultipart:
    """
    Create an email with the specified content.

    Args:
    subject (str): The subject of the email.
    text (str): The text content of the email. Defaults to an empty string.
    images (Optional[List[str]]): A list of image file paths. Defaults to None.
    attachments (Optional[List[str]]): A list of attachment file paths. Defaults to None.

    Returns:
    MIMEMultipart: The created email content.
    """
    email_content = MIMEMultipart()
    email_content["Subject"] = subject
    email_content.attach(MIMEText(text))

    if images is not None:
        if not isinstance(images, list):
            images = [images]

        for image in images:
            try:
                with open(image, "rb") as f:
                    image_data = f.read()
                email_content.attach(MIMEImage(image_data, name=os.path.basename(image)))
            except FileNotFoundError:
                print(f"Image file not found: {image}")

    if attachments is not None:
        if not isinstance(attachments, list):
            attachments = [attachments]

        for attachment in attachments:
            try:
                with open(attachment, "rb") as f:
                    file = MIMEApplication(f.read(), name=os.path.basename(attachment))
                file["Content-Disposition"] = f'attachment; filename="{os.path.basename(attachment)}"'
                email_content.attach(file)
            except FileNotFoundError:
                print(f"Attachment file not found: {attachment}")

    return email_content


def send_message(
    receiver_email: str,
    subject: str,
    text: str = "",
    images: Optional[List[str]] = None,
    attachments: Optional[List[str]] = None,
) -> None:
    """
    Create and send an email with the specified content.

    Args:
    receiver_email (str): The email address of the receiver.
    subject (str): The subject of the email.
    text (str): The text content of the email. Defaults to an empty string.
    images (Optional[List[str]]): A list of image file paths. Defaults to None.
    attachments (Optional[List[str]]): A list of attachment file paths. Defaults to None.
    """
    email_content = create_email(subject, text, images, attachments)
    send_email(receiver_email, email_content)


if __name__ == "__main__":
    message_text = """
    hey bhargav!!
    this mail is test email from python, with multiple attachments. 
    would love to hear comments from your side
    
    
    thank you!
    """
    subject = "mail with multiple attachments"

    send_message(
        "xyz@softnautics.com",
        subject,
        text=message_text,
        images=["/home/murtaza/Pictures/Screenshot from 2022-05-27 09-41-26.png"],
        attachments=["/home/murtaza/Documents/try1.txt"],
    )