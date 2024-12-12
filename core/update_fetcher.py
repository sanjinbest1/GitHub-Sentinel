from core.github_api import GitHubAPI
from core.subscription import SubscriptionManager

class UpdateFetcher:
    def __init__(self):
        self.github_api = GitHubAPI()
        self.subscription_manager = SubscriptionManager()

    def fetch_updates(self):
        updates = {}
        for repo_owner, repo_name in self.subscription_manager.get_subscriptions():
            updates[(repo_owner, repo_name)] = self.github_api.get_repo_updates(repo_owner, repo_name)
        return updates
