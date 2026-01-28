class ContributorDiversityEvaluator:

    def evaluate(self, contributors):
        count = len(contributors)

        if count >= 5:
            return {
                "status": "Low Risk",
                "score": 100
            }

        if count >= 2:
            return {
                "status": "Medium Risk",
                "score": 70
            }

        return {
            "status": "High Risk",
            "score": 30
        }
