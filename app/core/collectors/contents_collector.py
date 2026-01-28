
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
