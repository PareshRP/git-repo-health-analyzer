from app.core.collectors.github_client import GitHubClient

class ContributorsCollector:

    def __init__(self):
        self.client = GitHubClient()

    def get_contributors(self, owner, repo):
        endpoint = f"/repos/{owner}/{repo}/commits"
        params = {
            "per_page": 100
        }

        data = self.client.get(endpoint, params=params)

        contributors = set()

        for commit in data:
            author = commit.get("author")
            if author and author.get("login"):
                contributors.add(author["login"])

        return list(contributors)
