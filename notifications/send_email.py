import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv


class EmailNotifier:
    def __init__(self):
        load_dotenv()
        self.sender_email = os.getenv('EMAIL_USER')
        self.receiver_email = os.getenv('RECEIVER_EMAIL', 'my_email@example.com')
        self.password = os.getenv('EMAIL_PASS')

    def send_notification(self, subject, body):
        if not self.sender_email or not self.password:
            print("Email credentials are not set in the environment variables.")
            return

        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, msg.as_string())
            server.quit()
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")
