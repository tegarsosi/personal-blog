from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from dependencies import get_current_username
from services import BlogService

# Create the router
# Add 'dependencies' here to protect EVERY route in this file
router = APIRouter(
    prefix="/admin",
    dependencies=[Depends(get_current_username)]
)

templates = Jinja2Templates(directory="templates") # This tells FastAPI where my HTML files are
service = BlogService()

@router.get("/", response_class=HTMLResponse)
def admin_dashboard(request: Request):
    articles = service.get_all_articles()
    return templates.TemplateResponse(
        request=request,
        name="admin/dashboard.html",
        context={"articles": articles}
    )

@router.get("/add", response_class=HTMLResponse)
def add_article_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="admin/add.html",
        context={}
    )

@router.post("/add")
def handle_add_article(title: str = Form(...), content: str = Form(...)):
    service.create_article(title=title, content=content)
    return RedirectResponse(url="/", status_code=303) # 303 is the standard redirect code for "Post-then-Redirect"

@router.post("/delete/{article_id}")
def handle_delete_article(article_id: str):
    service.delete_article(article_id=article_id)
    return RedirectResponse(url="/admin", status_code=303)

@router.get("/edit/{article_id}", response_class=HTMLResponse)
def edit_article(request: Request, article_id: str):
    article = service.get_article_by_id(article_id)
    return templates.TemplateResponse(
        request=request,
        name="admin/edit.html",
        context={"article": article}
    )

@router.post("/edit/{article_id}")
def handle_edit_article(
    article_id: str,
    title: str = Form(...),
    content: str = Form(...)
):
    service.edit_article(
        article_id=article_id,
        title=title,
        content=content
    )
    return RedirectResponse(url="/admin", status_code=303)