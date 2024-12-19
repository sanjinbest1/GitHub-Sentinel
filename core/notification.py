import smtplib
from config.settings import NOTIFICATION_SETTINGS

class NotificationManager:
    def __init__(self):
        self.enabled = NOTIFICATION_SETTINGS['enabled']
        self.email = NOTIFICATION_SETTINGS['email']

    def send_notification(self, message):
        """
        Send a notification (for example, an email).
        :param message: The message to be sent
        """
        if self.enabled:
            # Here you can implement email or other types of notifications
            print(f"Sending notification to {self.email}: {message}")
        else:
            print("Notifications are disabled.")
