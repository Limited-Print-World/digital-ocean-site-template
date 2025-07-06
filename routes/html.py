from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import os,sys,time,json

root = Path(os.path.dirname( __file__ ))

templates = Jinja2Templates(directory=root/"templates")
forms = Jinja2Templates(directory=root/"templates/forms")
static = Jinja2Templates(directory=root/"static")
styles = Jinja2Templates(directory=root/"static/css")

resources = [
    templates,
    forms,
    static,
    styles
]

router = APIRouter()

verison = "0.0.3"

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "v_id": f"{verison}"})

@router.get("/credits", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("credits.html", {"request": request})

@router.get("/robots.txt", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("robots.txt", {"request": request})

@router.get("/rpg/survive", response_class=FileResponse)
async def index(request: Request):
    return templates.TemplateResponse("game.html", {"request": request})

@router.post("/submit-email", response_class=HTMLResponse)
async def submit_email(request: Request, email: str = Form(...)):
    return templates.TemplateResponse("submit-email.html", {
        "request": request,
        "message": f"Test Email submitted: {email}"
    })
@router.get("/forms", response_class=HTMLResponse)
async def get_forms(request: Request, email: str = Form(...)):
    links = []
    for page in os.listdir(forms): 
        links.append(page)
    return templates.TemplateResponse("forms.html", {
        "request": request,

        "form_collection": f"{links}"
    })
