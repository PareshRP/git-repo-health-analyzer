from app.core.collectors.commits_collector import CommitsCollector

collector = CommitsCollector()
commits = collector.get_commits_since("kubernetes", "kubernetes", 30)
print(len(commits))
print(commits[:3])
