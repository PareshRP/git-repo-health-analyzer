class SuggestionsEngine:

    def generate(self, metrics):

        suggestions = []

        commit = metrics.get("commit_activity")
        contributors = metrics.get("contributors")
        pr = metrics.get("pull_request_hygiene")
        ci = metrics.get("ci_cd")
        docs = metrics.get("documentation")

        # Commit Activity
        if commit in ["Stale", "Low"]:
            suggestions.append(
                "Increase commit frequency by encouraging smaller and more frequent merges."
            )

        # Contributors
        if contributors in ["High Risk", "Single Contributor"]:
            suggestions.append(
                "Reduce bus factor by encouraging more contributors and code reviewers."
            )

        # PR Hygiene
        if pr in ["Risky", "Poor"]:
            suggestions.append(
                "Introduce mandatory code reviews and reduce PR cycle time."
            )

        # CI/CD
        if ci == "Missing":
            suggestions.append(
                "Add a CI pipeline using GitHub Actions to run build and test workflows."
            )

        # Documentation
        if docs in ["Missing", "Weak"]:
            suggestions.append(
                "Add or improve README with setup instructions, usage examples, and contribution guide."
            )

        if not suggestions:
            suggestions.append(
                "Repository practices look healthy. Focus on scaling and automation."
            )

        return suggestions
