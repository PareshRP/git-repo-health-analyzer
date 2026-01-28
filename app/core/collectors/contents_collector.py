import base64
from app.core.collectors.github_client import GitHubClient

class ContentsCollector:

    def __init__(self):
        self.client = GitHubClient()

    def has_github_actions(self, owner, repo):
        endpoint = f"/repos/{owner}/{repo}/contents/.github/workflows"
        try:
            self.client.get(endpoint)
            return True
        except Exception:
            return False

    def get_readme_length(self, owner, repo):
        endpoint = f"/repos/{owner}/{repo}/readme"

        try:
            data = self.client.get(endpoint)
            content = base64.b64decode(data["content"]).decode("utf-8")
            return len(content)
        except Exception:
            return 0
