from pathlib import Path
from enum import Enum
import os,sys,time,json


from routes.forms import router as forms_router

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates



class FormName(str, Enum):
    generalQuery = "generalQuery"
    bulkRates = "bulkRates"
    figures = "figures"
    terrain = "terrain"


root = Path(os.path.dirname( __file__ )).parent

templates = Jinja2Templates(directory="templates")
forms = Jinja2Templates(directory="templates/forms")
static = Jinja2Templates(directory="static")
styles = Jinja2Templates(directory="static/css")

resources = [
    templates,
    forms,
    static,
    styles
]

router = APIRouter()

verison = "0.0.4"

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    varaible = "somethinGS"
    return templates.TemplateResponse("index.html", {"request": request,\
                                                     "v_id": f"{verison}"})

@router.get("/credits", response_class=HTMLResponse)
async def index(request: Request):
    def header(title="", level=3):
        """default page,"""
        decorator="*"
        return decorator*level + title.title() + decorator*level
    creditsList = [
        header("Graphical User Interface (GUI)"),
        'Sound Effect by <a href="https://pixabay.com/users/fronbondi_skegs-23154649/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=359401">Gavin Mogensen</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=359401">Pixabay</a>',
        header("sounds, effect, and ambience",),
        '',
    ]

    return templates.TemplateResponse("credits.html", {"request": request,\
                                                       "credList": creditsList})

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
        "message": email
    })

