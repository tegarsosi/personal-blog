from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from dependencies import check_credentials

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    if request.session.get("user"):
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse(request=request, name="login.html", context={})


@router.post("/login")
def handle_login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    if not check_credentials(username, password):
        return templates.TemplateResponse(
            request=request,
            name="login.html",
            context={"error": "Wrong username or password"},
            status_code=401,
        )
    request.session["user"] = username
    return RedirectResponse(url="/", status_code=303)


@router.post("/logout")
def handle_logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=303)