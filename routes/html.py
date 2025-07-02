from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import os,sys,time,json

root = Path(os.path.dirname( __file__ ))

templates = Jinja2Templates(directory="templates")
resources = Jinja2Templates(directory="static")
styles = Jinja2Templates(directory="static/css")


router = APIRouter()

verison = "0.0.3"

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "v_id": f"{verison}"})

@router.get("/rpg/survive", response_class=FileResponse)
async def index(request: Request):
    return templates.TemplateResponse("game.html", {"request": request})

@router.post("/submit-email", response_class=HTMLResponse)
async def submit_email(request: Request, email: str = Form(...)):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "message": f"Email submitted: {email}"
    })
