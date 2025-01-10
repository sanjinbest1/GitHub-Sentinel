import os
import json

SUBSCRIPTIONS_FILE = "config/subscriptions.json"

def load_subscriptions():
    """Load subscriptions from a JSON file."""
    if os.path.exists(SUBSCRIPTIONS_FILE):
        with open(SUBSCRIPTIONS_FILE, "r") as file:
            return json.load(file)
    return []

def save_subscriptions(subscriptions):
    """Save subscriptions to a JSON file."""
    with open(SUBSCRIPTIONS_FILE, "w") as file:
        json.dump(subscriptions, file, indent=4)

def add_subscription(repo):
    """Add a repository to the subscriptions list."""
    subscriptions = load_subscriptions()
    if repo not in subscriptions:
        subscriptions.append(repo)
        save_subscriptions(subscriptions)
        return f"Repository {repo} added to subscriptions."
    return f"Repository {repo} is already in subscriptions."

def remove_subscription(repo):
    """Remove a repository from the subscriptions list."""
    subscriptions = load_subscriptions()
    if repo in subscriptions:
        subscriptions.remove(repo)
        save_subscriptions(subscriptions)
        return f"Repository {repo} removed from subscriptions."
    return f"Repository {repo} is not in subscriptions."

def list_subscriptions():
    """Load subscriptions from a JSON file."""
    if os.path.exists(SUBSCRIPTIONS_FILE):
        with open(SUBSCRIPTIONS_FILE, "r") as file:
            subscriptions = json.load(file)
            # 确保读取的内容是完整的仓库名称列表
            if isinstance(subscriptions, list):
                return subscriptions
            else:
                return []
    return []

