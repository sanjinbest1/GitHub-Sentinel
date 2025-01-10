import requests
import datetime
from config.settings import GITHUB_TOKEN, GITHUB_API_URL

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

    def get_commits(self, owner, repo):
        """
        获取指定仓库的 commits 数据
        """
        commits_url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/commits"
        commits_response = requests.get(commits_url, headers=self.headers)

        if commits_response.status_code == 200:
            commits = commits_response.json()
            return commits
        else:
            raise Exception(f"Error fetching commits for {owner}/{repo}: {commits_response.status_code}")

    def save_to_markdown(self, owner, repo, issues, prs, commits):
        """
        将 issues、pull requests 和 commits 保存为 Markdown 格式的文件。
        """
        today = datetime.date.today().strftime("%Y-%m-%d")
        filename = f"data/progress/{repo}_{today}.md"

        with open(filename, "w") as f:
            f.write(f"# {repo} - {today}\n\n")
            f.write("## Issues\n")
            for issue in issues:
                f.write(f"- {issue['title']}: {issue['html_url']}\n")
            f.write("\n## Pull Requests\n")
            for pr in prs:
                f.write(f"- {pr['title']}: {pr['html_url']}\n")
            f.write("\n## Commits\n")
            for commit in commits:
                f.write(f"- {commit['commit']['message']}: {commit['html_url']}\n")
