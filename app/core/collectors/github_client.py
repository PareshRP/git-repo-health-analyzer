import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GitHubClient:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")

    def _headers(self):
        headers = {
            "Accept": "application/vnd.github+json"
        }

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        return headers

    def get(self, endpoint, params=None):
        url = f"{self.BASE_URL}{endpoint}"

        response = requests.get(
            url=url,
            headers=self._headers(),
            params=params
        )

        if response.status_code == 404:
            raise Exception("Resource not found")

        if response.status_code == 403:
            raise Exception("Forbidden or rate limit exceeded")

        if response.status_code >= 400:
            raise Exception(f"GitHub API error: {response.status_code}")

        return response.json()
