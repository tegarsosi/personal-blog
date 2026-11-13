from models import Article
from datetime import datetime, timezone
from sqlmodel import Session, select
from db import engine

class BlogService:
    def create_article(self, title: str, content: str) -> Article:
        article = Article(title=title, content=content)
        with Session(engine) as session:
            session.add(article)        # stage the insert
            session.commit()            # actually write it
            session.refresh(article)    # reload it from the DB
        return article

    def edit_article(self, article_id: str, title: str, content: str) -> Article | None:
        with Session(engine) as session:
            article = session.get(Article, article_id)
            if article is None:
                return None

            article.title = title
            article.content = content
            article.updated_at = datetime.now(timezone.utc)

            session.add(article)
            session.commit()
            session.refresh(article)
            
            return article
    
    def delete_article(self, article_id: str) -> None:
        with Session(engine) as session:
            article = session.get(Article, article_id)
            if article is not None:
                session.delete(article)
                session.commit()

    def get_all_articles(self) -> list[Article]:
        with Session(engine) as session:
            statement = select(Article).order_by(Article.updated_at.desc())
            return list(session.exec(statement).all())

    def get_article_by_id(self, article_id: str) -> Article | None:
        with Session(engine) as session:
            return session.get(Article, article_id)