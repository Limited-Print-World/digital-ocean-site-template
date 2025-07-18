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
form_templates = Jinja2Templates(directory="templates/forms")
static = Jinja2Templates(directory="static")
styles = Jinja2Templates(directory="static/css")

resources = [
    templates,
    form_templates,
    static,
    styles
]

router = APIRouter()


@router.get("/forms", response_class=HTMLResponse)
async def get_forms(request: Request, ):

    links = []
    
    for page in os.listdir(root/"templates/forms"): 
        pageName=page.split(".")[0]
        print("#"*6)

        print(pageName, page)
        print("#"*6)

        links.append(pageName)
    return templates.TemplateResponse("forms.html", {"request": request,"form_collection": links.copy() })
@router.get("/forms/{form_name}", response_class=HTMLResponse)
async def get_forms(request: Request, form_name:FormName):
    forms = FormName
    forms.generalQuery
    if form_name is forms.generalQuery:
        return form_templates.TemplateResponse(f"{form_name.generalQuery}.html", {"request": request,})
