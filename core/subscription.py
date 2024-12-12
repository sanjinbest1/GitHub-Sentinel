class SubscriptionManager:
    def __init__(self):
        self.subscriptions = []

    def add_subscription(self, repo_owner, repo_name):
        self.subscriptions.append((repo_owner, repo_name))

    def remove_subscription(self, repo_owner, repo_name):
        self.subscriptions.remove((repo_owner, repo_name))

    def get_subscriptions(self):
        return self.subscriptions
