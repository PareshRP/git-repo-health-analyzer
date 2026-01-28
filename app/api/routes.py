from fastapi import APIRouter, HTTPException
from app.services.analysis_service import AnalysisService

router = APIRouter()
service = AnalysisService()

@router.post("/analyze")
def analyze_repo(payload: dict):
    repo_url = payload.get("repo_url")

    if not repo_url:
        raise HTTPException(status_code=400, detail="repo_url is required")

    try:
        owner, repo = repo_url.replace("https://github.com/", "").split("/")
        return service.analyze(owner, repo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
