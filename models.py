from uuid import uuid4
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

class Article(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    title: str
    content: str
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)