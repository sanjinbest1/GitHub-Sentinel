import os
import cmd
from datetime import datetime
from core.github_api import GitHubClient
from llm.openai_llm import LLMClient
from core.report_generator import ReportGenerator
from core.subscription import add_subscription, remove_subscription, list_subscriptions

# 配置设置
OPENEAI_API_KEY = "sk-rwpBavDZX18kBqMCx5XeETDEGrqwQgaiFWgQIuA0IltTZ5dg"
OPENAI_PROXY_URL = "https://api.feidaapi.com/v1"  # 中转服务的 URL

# 初始化客户端
github_client = GitHubClient()
llm_client = LLMClient(OPENEAI_API_KEY)  # 传递中转服务的 URL
report_generator = ReportGenerator(llm_client)

class GitHubSentinelCLI(cmd.Cmd):
    intro = 'Welcome to GitHub Sentinel! Type help or ? to list commands.\n'
    prompt = '(GitHub-Sentinel) '

    def do_fetch(self, arg):
        """Fetch issues, pull requests and generate reports for all subscribed repositories."""
        today = datetime.today().strftime("%Y-%m-%d")
        subscriptions = list_subscriptions()

        if not subscriptions:
            print("No repositories are currently subscribed to.")
            return

        # 获取并保存每日进展
        for repo in subscriptions:
            owner, repo_name = repo.split("/")

            # 获取仓库的 issues 和 PRs 列表
            issues, prs = github_client.get_issues_and_prs(owner, repo_name)

            # 将数据保存为 Markdown 文件
            github_client.save_to_markdown(repo_name, issues, prs)
            print(f"Progress saved for {repo_name} - {today}")

        # 为每个仓库生成每日报告
        for repo in subscriptions:
            owner, repo_name = repo.split("/")
            report_filename = report_generator.generate_report(repo_name, today)
            print(f"Report generated for {repo_name} - {today}: {report_filename}")

    def do_report(self, arg):
        """Generate reports for all subscribed repositories."""
        today = datetime.today().strftime("%Y-%m-%d")
        subscriptions = list_subscriptions()

        if not subscriptions:
            print("No repositories are currently subscribed to.")
            return

        for repo in subscriptions:
            owner, repo_name = repo.split("/")
            report_filename = report_generator.generate_report(repo_name, today)
            print(f"Report generated for {repo_name} - {today}: {report_filename}")

    def do_subscribe(self, repo):
        """Subscribe to a repository (format: owner/repo)."""
        if repo:
            result = add_subscription(repo)
            print(result)
        else:
            print("Please provide a repository to subscribe to.")

    def do_unsubscribe(self, repo):
        """Unsubscribe from a repository (format: owner/repo)."""
        if repo:
            result = remove_subscription(repo)
            print(result)
        else:
            print("Please provide a repository to unsubscribe from.")

    def do_list(self, arg):
        """List all subscribed repositories."""
        subscriptions = list_subscriptions()

        if subscriptions:
            print("Subscribed repositories:")
            for repo in subscriptions:
                print(f"- {repo}")
        else:
            print("No repositories found.")

    def do_exit(self, arg):
        """Exit the application."""
        print("Goodbye!")
        return True

if __name__ == "__main__":
    GitHubSentinelCLI().cmdloop()
