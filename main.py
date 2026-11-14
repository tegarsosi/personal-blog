from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from services import BlogService
from routers import admin, auth
from dependencies import require_login
from db import init_db
from starlette.middleware.sessions import SessionMiddleware
import os

app = FastAPI()
app.add_middleware(
    SessionMiddleware,
    secret_key=os.environ["SECRET_KEY"],
    https_only=bool(os.getenv("VERCEL")),
    same_site="lax",
)
init_db()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates") # This tells FastAPI where your HTML files are
service = BlogService()

app.include_router(admin.router)
app.include_router(auth.router)

@app.get("/", response_class=HTMLResponse, dependencies=[Depends(require_login)])
def home_page(request: Request):
    articles = service.get_all_articles()
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"articles": articles}
    )

@app.get("/article/{article_id}", response_class=HTMLResponse, dependencies=[Depends(require_login)])
def get_article(request: Request, article_id: str):
    article = service.get_article_by_id(article_id)
    return templates.TemplateResponse(
        request=request,
        name="article.html",
        context={"article": article}
    )
