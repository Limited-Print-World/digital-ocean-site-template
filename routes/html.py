from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

import os,sys,time,json


from enum import Enum

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
async def get_forms(request: Request, ):
    links = []
    for page in os.listdir(root/"templates/forms"): 
        pageName= page.split(".")[0]
        print("#"*6)

        print(pageName, page)
        print("#"*6)

        links.append(pageName)
    return templates.TemplateResponse("forms.html", {"request": request,"form_collection": links.copy() })
@router.get("/forms/{form_name}", response_class=HTMLResponse)
async def get_forms(request: Request, form_name:FormName):
    if form_name is form_name.generalQuery:
        return forms.TemplateResponse(f"{form_name.generalQuery}.html", {"request": request,})
