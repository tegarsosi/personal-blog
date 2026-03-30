import json
import uuid
from pathlib import Path
from datetime import datetime
from pydantic import BaseModel, Field

class Article(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    content: str
    published_at: datetime = Field(default_factory=datetime.now)

class BlogService:
    def __init__(self, storage_dir: str = "storage"):
        self.storage_path = Path(storage_dir)
        # Ensure the directory exists immediately
        self.storage_path.mkdir(exist_ok=True)

    def create_article(self, title: str, content: str) -> Article:
        article = Article(title=title, content=content)
        file_path = self.storage_path / f"{article.id}.json"

        with open(file_path, "w") as f:
            f.write(article.model_dump_json())

        return article
    
    def delete_article(self, article_id: str) -> None:
        file_path = self.storage_path / f"{article_id}.json"
        if file_path.exists():
            file_path.unlink() # This deletes the file

    def get_all_articles(self) -> list[Article]:
        articles = []
        for file in self.storage_path.glob("*.json"):
            with open(file, "r") as f:
                data = json.load(f)
                articles.append(Article(**data))

        # Sort by date: Latest first
        articles.sort(key=lambda x: x.published_at, reverse=True)
        return articles

    def get_article_by_id(self, article_id: str) -> Article | None:
        file_path = self.storage_path / f"{article_id}.json"
        if not file_path.exists():
            return None

        with open(file_path, "r") as f:
            return Article.model_validate_json(f.read())