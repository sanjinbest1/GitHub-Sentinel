from datetime import datetime
from core.clients import initialize_clients  # 引入初始化客户端的函数
from core.subscription import list_subscriptions

# 使用统一的客户端初始化函数
github_client, llm_client, report_generator = initialize_clients()

def fetch_and_generate_reports():
    """
    获取所有订阅仓库的 issues、pull request 和 commits 更新，并生成报告。
    """
    today = datetime.now().strftime("%Y-%m-%d")

    # 获取并保存每日进展
    for repo in list_subscriptions():
        owner, repo_name = repo.split("/")

        # 获取仓库的 issues 和 PRs 列表
        issues, prs = github_client.get_issues_and_prs(owner, repo_name)

        # 获取 commits
        commits = github_client.get_commits(owner, repo_name)

        # 将数据保存为 Markdown 文件
        github_client.save_to_markdown(owner, repo_name, issues, prs, commits)
        print(f"Progress saved for {repo_name} - {today}")

    # 为每个仓库生成每日报告
    for repo in list_subscriptions():
        owner, repo_name = repo.split("/")
        report_filename = report_generator.generate_report(repo_name, today)
        print(f"Report generated for {repo_name} - {today}: {report_filename}")

def generate_reports():
    """
    为所有订阅的仓库生成报告。
    """
    today = datetime.now().strftime("%Y-%m-%d")
    subscriptions = list_subscriptions()
    if not subscriptions:
        print("No repositories are subscribed to.")
        return

    for repo in subscriptions:
        owner, repo_name = repo.split("/")
        report_filename = report_generator.generate_report(repo_name, today)
        print(f"Report generated: {report_filename}")
