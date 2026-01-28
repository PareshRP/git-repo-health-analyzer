from app.core.collectors.github_client import GitHubClient

class RepoCollector:

    def __init__(self):
        self.client = GitHubClient()

    def get_repository(self, owner, repo):
        endpoint = f"/repos/{owner}/{repo}"
        data = self.client.get(endpoint)

        return {
            "full_name": data.get("full_name"),
            "default_branch": data.get("default_branch"),
            "created_at": data.get("created_at"),
            "updated_at": data.get("updated_at"),
            "language": data.get("language")
        }
