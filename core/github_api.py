import requests
import datetime
from config.settings import GITHUB_TOKEN, GITHUB_API_URL
import os

class GitHubClient:
    def __init__(self):
        self.headers = {
            'Authorization': f'token {GITHUB_TOKEN}'
        }

    def get_issues_and_prs(self, owner, repo):
        """
        获取指定仓库的所有 issues 和 pull requests。
        """
        issues_url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues?state=all"
        prs_url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls?state=open"

        issues_response = requests.get(issues_url, headers=self.headers)
        prs_response = requests.get(prs_url, headers=self.headers)

        if issues_response.status_code == 200 and prs_response.status_code == 200:
            issues = issues_response.json()
            prs = prs_response.json()
            return issues, prs
        else:
            raise Exception(f"Error fetching issues or PRs for {owner}/{repo}: {issues_response.status_code}, {prs_response.status_code}")

    import os

    def save_to_markdown(self, repo, issues, prs):
        """
        将 issues 和 pull requests 保存为 Markdown 格式的文件。
        文件名格式：repo_YYYY-MM-DD.md
        """
        today = datetime.date.today().strftime("%Y-%m-%d")
        # 设置文件保存路径
        directory = "data/progress"
        filename = f"{directory}/{repo}_{today}.md"

        # 如果目录不存在，则创建它
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 打开文件并写入内容
        with open(filename, "w") as f:
            f.write(f"# {repo} - {today}\n\n")
            f.write("## Issues\n")
            for issue in issues:
                f.write(f"- {issue['title']}: {issue['html_url']}\n")
            f.write("\n## Pull Requests\n")
            for pr in prs:
                f.write(f"- {pr['title']}: {pr['html_url']}\n")


    def fetch_latest_release(self, repo):
        """
        获取指定 GitHub 仓库的最新发布版本。
        :param repo: GitHub 仓库名称 (例如 'owner/repo')
        :return: JSON 响应，包含发布版本数据
        """
        url = f'{GITHUB_API_URL}/repos/{repo}/releases/latest'
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()  # 返回最新发布版本的数据
        else:
            raise Exception(f"Error fetching latest release for {repo}: {response.status_code}")

    def fetch_repo_info(self, repo):
        """
        获取指定 GitHub 仓库的基本信息。
        :param repo: GitHub 仓库名称 (例如 'owner/repo')
        :return: JSON 响应，包含仓库信息
        """
        url = f'{GITHUB_API_URL}/repos/{repo}'
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()  # 返回仓库信息
        else:
            raise Exception(f"Error fetching repo info for {repo}: {response.status_code}")
