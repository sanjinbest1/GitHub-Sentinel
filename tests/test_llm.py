import requests
import json

class LLMClient:
    def __init__(self, api_key):
        self.api_key = api_key  # 设置 API 密钥
        self.api_url = "https://mj.cxhao.com/v1/chat/completions"  # OpenAI API URL

    def summarize(self, issues, prs):
        """
        使用 GPT-3.5 或 GPT-4 API 对 issues 和 pull requests 进行总结。
        """
        prompt = f"""
        请总结以下内容：

        Issues:
        {issues}

        Pull Requests:
        {prs}

        总结如下：
        """

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "gpt-3.5-turbo",  # 你可以根据权限改为 gpt-4
            "messages": [
                {"role": "system", "content": "你是一个高效的技术总结助手，帮助开发团队总结任务和进展。"},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 500,  # 控制生成的最大字符数
            "temperature": 0.7  # 控制生成内容的创意程度
        }

        # 发送 POST 请求到 OpenAI API
        response = requests.post(self.api_url, headers=headers, data=json.dumps(data))

        print(response.text)


if __name__ == '__main__':
    api_key = "sk-rwpBavDZX18kBqMCx5XeETDEGrqwQgaiFWgQIuA0IltTZ5dg"
    llm_client = LLMClient(api_key)
    issues = "Issue 1\nIssue 2\n..."
    prs = "PR 1\nPR 2\n..."
    summary = llm_client.summarize(issues, prs)
