class CIPresenceEvaluator:

    def evaluate(self, has_ci):
        if has_ci:
            return {"status": "Present", "score": 100}

        return {"status": "Missing", "score": 30}
