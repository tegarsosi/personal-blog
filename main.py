from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from services import BlogService
from routers import admin


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates") # This tells FastAPI where your HTML files are
service = BlogService()

app.include_router(admin.router)

@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    articles = service.get_all_articles()
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"articles": articles}
    )

@app.get("/article/{article_id}", response_class=HTMLResponse)
def get_article(request: Request, article_id: str):
    article = service.get_article_by_id(article_id)
    return templates.TemplateResponse(
        request=request,
        name="article.html",
        context={"article": article}
    )
