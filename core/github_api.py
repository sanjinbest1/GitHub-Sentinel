import requests
from config.settings import GITHUB_TOKEN, GITHUB_API_URL

# Set up headers with authorization
headers = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

def fetch_latest_release(repo):
    """
    Fetch the latest release from the specified GitHub repository.
    :param repo: GitHub repository name (e.g., 'owner/repo')
    :return: JSON response with release data
    """
    url = f'{GITHUB_API_URL}/repos/{repo}/releases/latest'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Return the latest release data
    else:
        raise Exception(f"Error fetching data for {repo}: {response.status_code}")

def fetch_repo_info(repo):
    """
    Fetch repository information from GitHub.
    :param repo: GitHub repository name (e.g., 'owner/repo')
    :return: JSON response with repository data
    """
    url = f'{GITHUB_API_URL}/repos/{repo}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Return repository info
    else:
        raise Exception(f"Error fetching repo data for {repo}: {response.status_code}")
