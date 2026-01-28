class SuggestionsEngine:

    def generate(self, metrics):

        suggestions = []

        commit = metrics["commit_activity"]["status"]
        contributors = metrics["contributors"]["status"]
        pr = metrics["pr_hygiene"]["status"]
        ci = metrics["ci_presence"]["status"]
        docs = metrics["documentation"]["status"]

        if commit in ["Stale", "Low"]:
            suggestions.append(
                "Increase commit frequency by encouraging smaller and more frequent merges."
            )

        if contributors in ["High Risk", "Single Contributor"]:
            suggestions.append(
                "Reduce bus factor by encouraging more contributors and code reviewers."
            )

        if pr in ["Risky", "Poor"]:
            suggestions.append(
                "Introduce mandatory code reviews and reduce PR cycle time."
            )

        if ci == "Missing":
            suggestions.append(
                "Add a CI pipeline using GitHub Actions to run build and test workflows."
            )

        if docs in ["Missing", "Weak"]:
            suggestions.append(
                "Add or improve README with setup instructions, usage examples, and contribution guide."
            )

        if not suggestions:
            suggestions.append(
                "Repository practices look healthy. Focus on scaling and automation."
            )

        return suggestions
