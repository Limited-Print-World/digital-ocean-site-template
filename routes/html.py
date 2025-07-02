from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
resources = Jinja2Templates(directory="static")
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/favicon.ico", response_class=FileResponse)
def get_favicon(request: FileResponse):
    '''adds a favicon to the title.'''
    return resources.TemplateResponse("static/favicon.ico")
@router.get("/img/favicon.ico", response_class=FileResponse)
def get_favicon(request: FileResponse):
    '''adds a favicon to the title.'''
    return resources.TemplateResponse("static/img/favicon.ico")
@router.get("/img/raven_head_left.png", response_class=FileResponse)
def get_favicon(request: FileResponse):
    '''adds a favicon to the title.'''
    return resources.TemplateResponse("static/img/raven_head_left.png")
@router.post("/submit-email", response_class=HTMLResponse)
async def submit_email(request: Request, email: str = Form(...)):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "message": f"Email submitted: {email}"
    })
