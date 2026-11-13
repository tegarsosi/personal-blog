import json
from pathlib import Path
from sqlmodel import Session
from datetime import datetime, timezone

from db import engine, init_db
from models import Article

init_db()

with Session(engine) as session:
    for file in Path("storage").glob("*.json"):
        data = json.loads(file.read_text())
        article = Article.model_validate(data)
        article.created_at = article.created_at.astimezone(timezone.utc)
        article.updated_at = article.updated_at.astimezone(timezone.utc)

        if session.get(Article, article.id):
            print(f"skip (already exists): {article.title}")
            continue

        session.add(article)
        print(f"imported: {article.title}")

    session.commit()