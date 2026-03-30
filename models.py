import uuid
from datetime import datetime
from pydantic import BaseModel, Field

class Article(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    content: str
    published_at: datetime = Field(default_factory=datetime.now)