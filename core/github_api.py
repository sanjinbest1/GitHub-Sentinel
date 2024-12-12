import requests
from config import settings

class GitHubAPI:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {settings.GITHUB_TOKEN}"
        }

    def get_repo_updates(self, repo_owner, repo_name):
        url = f"{self.base_url}/repos/{repo_owner}/{repo_name}/events"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()  # Returns a list of events for the repo
        else:
            raise Exception(f"Error fetching updates: {response.status_code}")
