from app.core.collectors.github_client import GitHubClient

client = GitHubClient()
print(client.get("/repos/kubernetes/kubernetes")["full_name"])