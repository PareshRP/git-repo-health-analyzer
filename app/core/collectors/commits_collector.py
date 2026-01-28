from datetime import datetime, timedelta
from app.core.collectors.github_client import GitHubClient

class CommitsCollector:

    def __init__(self):
        self.client = GitHubClient()

    def get_commits_since(self, owner, repo, days):
        since_date = datetime.utcnow() - timedelta(days=days)
        since_iso = since_date.isoformat() + "Z"

        endpoint = f"/repos/{owner}/{repo}/commits"

        params = {
            "since": since_iso,
            "per_page": 100
        }

        data = self.client.get(endpoint, params=params)

        return [
            commit["commit"]["author"]["date"]
            for commit in data
            if commit.get("commit")
        ]
