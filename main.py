from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from services import BlogService


app = FastAPI()
templates = Jinja2Templates(directory="templates") # This tells FastAPI where your HTML files are
service = BlogService()

@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    articles = service.get_all_articles()
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"articles": articles}
    )

@app.get("/admin/add", response_class=HTMLResponse)
def add_article_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="admin/add.html"
    )

@app.post("/admin/add")
def handle_add_article(
    request: Request,
    title: str = Form(...),
    content: str = Form(...)
):
    service.create_article(title=title, content=content)
    return RedirectResponse(url="/", status_code=303) # 303 is the standard redirect code for "Post-then-Redirect"