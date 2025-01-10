import requests
import json
from config.settings import OPENAI_API_KEY,OPENAI_PROXY_URL

class LLMClient:

    def summarize(self, issues, prs, commits):
        completions_url = OPENAI_PROXY_URL + "/v1/chat/completions"

        """
        使用 GPT-4 API 对 issues、pull requests 和 commits 进行总结。
        """
        prompt = f"""
        请总结以下内容：

        Issues:
        {issues}

        Pull Requests:
        {prs}

        Commits:
        {commits}

        总结如下：
        """

        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "gpt-3.5-turbo",  # 你可以根据权限改为 gpt-4
            "messages": [
                {"role": "system", "content": "你是一个高效的技术总结助手，帮助开发团队总结任务和进展。"},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 500,
            "temperature": 0.7
        }

        # 发送 POST 请求到 OpenAI API
        response = requests.post(completions_url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
