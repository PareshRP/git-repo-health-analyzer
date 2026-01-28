from app.core.collectors.repo_collector import RepoCollector
from app.core.collectors.commits_collector import CommitsCollector
from app.core.collectors.contributors_collector import ContributorsCollector
from app.core.collectors.prs_collector import PRsCollector
from app.core.collectors.contents_collector import ContentsCollector

from app.core.evaluators.commit_activity import CommitActivityEvaluator
from app.core.evaluators.contributor_diversity import ContributorDiversityEvaluator
from app.core.evaluators.pr_hygiene import PRHygieneEvaluator
from app.core.evaluators.ci_presence import CIPresenceEvaluator
from app.core.evaluators.documentation_quality import DocumentationQualityEvaluator

from app.core.scoring.aggregator import ScoreAggregator

from app.storage.cache_repository import CacheRepository


class AnalysisService:

    def analyze(self, owner, repo):

        cache = CacheRepository()
        repo_key = f"{owner}/{repo}"

        cached = cache.get(repo_key)
        if cached:
            return cached

        # Validate repo
        RepoCollector().get_repository(owner, repo)

        # Collect data
        commits = CommitsCollector().get_commits_since(owner, repo, 30)
        contributors = ContributorsCollector().get_contributors(owner, repo)
        prs = PRsCollector().get_recent_prs(owner, repo)
        contents = ContentsCollector()

        has_ci = contents.has_github_actions(owner, repo)
        readme_length = contents.get_readme_length(owner, repo)

        # Evaluate metrics
        commit_result = CommitActivityEvaluator().evaluate(commits)
        contributor_result = ContributorDiversityEvaluator().evaluate(contributors)
        pr_result = PRHygieneEvaluator().evaluate(prs)
        ci_result = CIPresenceEvaluator().evaluate(has_ci)
        doc_result = DocumentationQualityEvaluator().evaluate(readme_length)

        metrics = {
            "commit_activity": commit_result,
            "contributors": contributor_result,
            "pr_hygiene": pr_result,
            "ci_presence": ci_result,
            "documentation": doc_result
        }

        # Aggregate score
        final = ScoreAggregator().aggregate(metrics)

        result = {
            "repository": f"{owner}/{repo}",
            "health_score": final["score"],
            "status": final["status"],
            "metrics": {
                "commit_activity": commit_result["status"],
                "contributors": contributor_result["status"],
                "pull_request_hygiene": pr_result["status"],
                "ci_cd": ci_result["status"],
                "documentation": doc_result["status"]
            }
        }

        cache.save(repo_key, result)
        return result

