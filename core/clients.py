from core.github_api import GitHubClient
from llm.openai_llm import LLMClient
from core.report_generator import ReportGenerator

def initialize_clients():
    """
    初始化所有客户端（GitHub API 客户端、LLM 客户端、报告生成器）
    :return: 返回初始化的 GitHubClient, LLMClient 和 ReportGenerator 实例
    """
    # 初始化 GitHub 客户端
    github_client = GitHubClient()

    # 初始化 LLM 客户端
    llm_client = LLMClient()

    # 初始化报告生成器
    report_generator = ReportGenerator(llm_client)

    return github_client, llm_client, report_generator
