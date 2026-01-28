class CommitActivityEvaluator:

    def evaluate(self, commit_dates):
        count = len(commit_dates)

        if count >= 20:
            return {
                "status": "Healthy",
                "score": 100
            }

        if count >= 5:
            return {
                "status": "Moderate",
                "score": 70
            }

        return {
            "status": "Stale",
            "score": 30
        }
