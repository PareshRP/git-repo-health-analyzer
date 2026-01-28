from datetime import datetime, timedelta
from app.core.collectors.github_client import GitHubClient

class PRsCollector:

    def __init__(self):
        self.client = GitHubClient()

    def get_recent_prs(self, owner, repo, days=90):
        since_date = datetime.utcnow() - timedelta(days=days)
        endpoint = f"/repos/{owner}/{repo}/pulls"

        params = {
            "state": "all",
            "per_page": 100,
            "sort": "updated",
            "direction": "desc"
        }

        data = self.client.get(endpoint, params=params)

        recent_prs = []

        for pr in data:
            updated = pr.get("updated_at")
            if not updated:
                continue

            updated_dt = datetime.fromisoformat(updated.replace("Z", ""))
            if updated_dt < since_date:
                break

            recent_prs.append({
                "created_at": pr.get("created_at"),
                "merged_at": pr.get("merged_at"),
                "state": pr.get("state")
            })

        return recent_prs
