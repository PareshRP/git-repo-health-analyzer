import json
from datetime import datetime, timedelta
from app.storage.database import get_connection

CACHE_TTL_HOURS = 24

class CacheRepository:

    def __init__(self):
        self._init_table()

    def _init_table(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS repo_cache (
            repo TEXT PRIMARY KEY,
            result TEXT,
            created_at TEXT
        )
        """)

        conn.commit()
        conn.close()

    def get(self, repo):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT result, created_at FROM repo_cache WHERE repo=?",
            (repo,)
        )

        row = cursor.fetchone()
        conn.close()

        if not row:
            return None

        result_json, created_at = row
        created_at = datetime.fromisoformat(created_at)

        if datetime.utcnow() - created_at > timedelta(hours=CACHE_TTL_HOURS):
            return None

        return json.loads(result_json)

    def save(self, repo, result):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT OR REPLACE INTO repo_cache(repo, result, created_at)
        VALUES (?, ?, ?)
        """, (
            repo,
            json.dumps(result),
            datetime.utcnow().isoformat()
        ))

        conn.commit()
        conn.close()
