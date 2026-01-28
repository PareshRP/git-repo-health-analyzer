from app.core.scoring.weights import METRIC_WEIGHTS

class ScoreAggregator:

    def aggregate(self, metric_results):
        total = 0

        for name, result in metric_results.items():
            weight = METRIC_WEIGHTS.get(name, 0)
            total += result["score"] * weight

        final_score = round(total)

        if final_score >= 80:
            status = "Healthy"
        elif final_score >= 60:
            status = "Needs Attention"
        else:
            status = "At Risk"

        return {
            "score": final_score,
            "status": status
        }
