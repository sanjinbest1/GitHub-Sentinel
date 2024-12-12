import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class NotificationSystem:
    def send_email(self, to_email, subject, body):
        msg = MIMEMultipart()
        msg["From"] = "your_email@example.com"
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP("smtp.example.com") as server:
            server.login("your_email@example.com", "password")
            server.sendmail(msg["From"], msg["To"], msg.as_string())

    def send_slack_notification(self, channel, message):
        # Slack integration
        pass
