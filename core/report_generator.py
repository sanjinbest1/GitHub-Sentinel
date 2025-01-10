import os

class ReportGenerator:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def generate_report(self, repo_name, date):
        """
        生成项目的每日报告，基于进展文件和 GPT-4 总结。
        """
        # 读取进展文件
        filename = f"data/progress/{repo_name}_{date}.md"
        if not os.path.exists(filename):
            return f"No progress file found for {repo_name} on {date}"

        with open(filename, "r") as f:
            content = f.read()

        # 提取 Issues 和 PRs 部分
        issues_start = content.find("## Issues") + len("## Issues\n")
        prs_start = content.find("## Pull Requests") + len("## Pull Requests\n")
        issues = content[issues_start:prs_start].strip()
        prs = content[prs_start:].strip()

        # 调用 GPT-4 API 生成报告
        report = self.llm_client.summarize(issues, prs)

        # 保存生成的报告
        report_dir = "data/reports"
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)

        report_filename = f"data/reports/{repo_name}_{date}_report.md"
        with open(report_filename, "w") as f:
            f.write(f"# {repo_name} Daily Report - {date}\n\n")
            f.write(report)

        return f"Report generated: {report_filename}"
