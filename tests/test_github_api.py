import unittest
from core.github_api import fetch_latest_release


class TestGitHubAPI(unittest.TestCase):
    def test_fetch_latest_release(self):
        repo = 'langchain-ai/langchain'
        release = fetch_latest_release(repo)
        print(release)
        self.assertIsNotNone(release)
        self.assertIn('tag_name', release)

if __name__ == '__main__':
    unittest.main()
# Add tests for GitHub API interactions here
