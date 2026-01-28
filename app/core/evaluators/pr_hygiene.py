from datetime import datetime

class PRHygieneEvaluator:

    def evaluate(self, prs):
        if not prs:
            return {
                "status": "No Data",
                "score": 50
            }

        merged = [p for p in prs if p["merged_at"]]
        merge_rate = len(merged) / len(prs)

        cycle_times = []

        for p in merged:
            created = datetime.fromisoformat(p["created_at"].replace("Z", ""))
            merged_at = datetime.fromisoformat(p["merged_at"].replace("Z", ""))
            cycle_times.append((merged_at - created).total_seconds() / 3600)

        avg_cycle_hours = sum(cycle_times) / len(cycle_times) if cycle_times else 0

        if merge_rate >= 0.7 and avg_cycle_hours <= 72:
            return {"status": "Healthy", "score": 100}

        if merge_rate >= 0.4:
            return {"status": "Acceptable", "score": 70}

        return {"status": "Risky", "score": 30}
