import cmd
from _datetime import datetime
from core.github_api import GitHubClient
from core.report_generator import ReportGenerator
from llm.openai_llm import LLMClient
from core.subscription import add_subscription, remove_subscription, list_subscriptions

# 初始化客户端
github_client = GitHubClient()
llm_client = LLMClient()
report_generator = ReportGenerator(llm_client)

class GitHubSentinelCLI(cmd.Cmd):
    prompt = "(GitHub Sentinel) "

    def do_fetch(self, arg):
        """Fetch and generate progress and reports for subscribed repositories."""
        today = datetime.now().strftime("%Y-%m-%d")

        # 获取并保存每日进展
        for repo in list_subscriptions():
            owner, repo_name = repo.split("/")

            # 获取仓库的 issues 和 PRs 列表
            issues, prs = github_client.get_issues_and_prs(owner, repo_name)

            commits = github_client.get_commits(owner, repo_name)

            # 将数据保存为 Markdown 文件
            github_client.save_to_markdown(owner, repo_name, issues, prs, commits)
            print(f"Progress saved for {repo_name} - {today}")

        # 为每个仓库生成每日报告
        for repo in list_subscriptions():
            owner, repo_name = repo.split("/")
            report_filename = report_generator.generate_report(repo_name, today)
            print(f"Report generated for {repo_name} - {today}: {report_filename}")

    def do_report(self, arg):
        """Generate reports for all subscribed repositories."""
        today = datetime.now().strftime("%Y-%m-%d")
        subscriptions = list_subscriptions()
        if not subscriptions:
            print("No repositories are subscribed to. Please subscribe to a repository first.")
            return
        for repo in subscriptions:
            owner, repo_name = repo.split("/")
            report_filename = report_generator.generate_report(repo_name, today)
            print(f"Report generated: {report_filename}")

    def do_subscribe(self, repo):
        """Subscribe to a repository."""
        if not repo:
            print("Repository name is required to subscribe.")
        else:
            print(add_subscription(repo))

    def do_unsubscribe(self, repo):
        """Unsubscribe from a repository."""
        if not repo:
            print("Repository name is required to unsubscribe.")
        else:
            print(remove_subscription(repo))

    def do_list(self, arg):
        """List all subscribed repositories."""
        subscriptions = list_subscriptions()
        if subscriptions:
            print("Subscribed repositories:")
            for repo in subscriptions:
                print(f"- {repo}")
        else:
            print("No subscriptions found.")

    def do_exit(self, arg):
        """Exit the command-line interface."""
        print("Exiting GitHub Sentinel CLI.")
        return True

    def do_help(self, arg):
        """Display help message for supported commands."""
        print("""
Supported commands:

  fetch        - Fetch and generate progress and reports for all subscribed repositories
  report       - Generate reports for all subscribed repositories
  subscribe    - Subscribe to a repository. Usage: subscribe <repo_name>
  unsubscribe  - Unsubscribe from a repository. Usage: unsubscribe <repo_name>
  list         - List all subscribed repositories
  exit         - Exit the CLI
  help         - Show this help message
""")

def main():
    print("Welcome to GitHub Sentinel CLI!")
    print("Type 'help' to see available commands.")
    cli = GitHubSentinelCLI()
    cli.cmdloop()

if __name__ == "__main__":
    main()
