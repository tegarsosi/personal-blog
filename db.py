import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine

load_dotenv()

url = os.getenv("DATABASE_URL", "sqlite:///blog.db")
url = url.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(url)

def init_db():
    SQLModel.metadata.create_all(engine)