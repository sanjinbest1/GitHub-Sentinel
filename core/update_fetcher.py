
from core.github_api import GitHubClient
from core.report_generator import ReportGenerator
from core.subscription import load_subscriptions

class UpdateFetcher:


    def __init__(self, repo):
        self.repo = repo

    def get_latest_update(self):
        # 初始化 GitHubClient
        github_client = GitHubClient()
        """
        Fetch the latest release of the repository.
        :return: Latest release data
        """
        try:
            return github_client.fetch_latest_release(self.repo)
        except Exception as e:
            print(f"Error fetching updates: {e}")
            return None


#
# def fetch_and_generate_reports():
#     # 初始化 GitHubClient
#     github_client = GitHubClient()
#     reportGenerator = ReportGenerator()
#     """Fetch and generate reports for all subscribed repositories."""
#     subscriptions = load_subscriptions()
#     for repo in subscriptions:
#         try:
#             print(f"Fetching latest release for {repo}...")
#             latest_release = github_client.fetch_latest_release(repo)
#             report_path = reportGenerator.generate_report(latest_release, repo)
#             print(f"Report generated: {report_path}")
#         except Exception as e:
#             print(f"Failed to fetch updates for {repo}: {e}")
