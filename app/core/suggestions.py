class SuggestionsEngine:

    def generate(self, metrics):

        suggestions = []

        if metrics["commit_activity"] == "Stale":
            suggestions.append(
                "Increase commit frequency by enforcing smaller, more frequent merges."
            )

        if metrics["contributors"] == "High Risk":
            suggestions.append(
                "Reduce single-contributor risk by encouraging more engineers to contribute."
            )

        if metrics["pull_request_hygiene"] == "Risky":
            suggestions.append(
                "Improve PR hygiene by enforcing reviews and reducing PR cycle time."
            )

        if metrics["ci_cd"] == "Missing":
            suggestions.append(
                "Add a GitHub Actions workflow for automated build and tests."
            )

        if metrics["documentation"] == "Missing":
            suggestions.append(
                "Add a README with setup, usage, and contribution guidelines."
            )

        if not suggestions:
            suggestions.append(
                "Repository practices look healthy. Focus on continuous improvement."
            )

        return suggestions
