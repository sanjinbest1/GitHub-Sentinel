import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("/Users/lixin/work/workspace/GitHub-Sentinel/development.env")

# GitHub Token from environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# GitHub API base URL
GITHUB_API_URL = 'https://api.github.com'

# Notification settings (example: can be extended to support email/SMS notifications)
NOTIFICATION_SETTINGS = {
    'enabled': True,
    'email': 'sanjinbest1@gmail.com',  # Email for notifications (example)
}
