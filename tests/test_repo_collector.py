from app.core.collectors.repo_collector import RepoCollector

collector = RepoCollector()
repo = collector.get_repository("kubernetes", "kubernetes")
print(repo)
