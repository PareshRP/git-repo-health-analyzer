class DocumentationQualityEvaluator:

    def evaluate(self, readme_length):
        if readme_length >= 300:
            return {"status": "Good", "score": 100}

        if readme_length > 0:
            return {"status": "Weak", "score": 70}

        return {"status": "Missing", "score": 30}
