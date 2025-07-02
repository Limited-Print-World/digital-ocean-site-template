from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import httpx

router = APIRouter(prefix="/dev/logs")
templates = Jinja2Templates(directory="templates")

GITHUB_USER = "pitherbro"          # replace with your GitHub user/org
GITHUB_REPO = "digital-ocean-site-template"      # replace with your repo

@router.get("/git")
async def github_logs(request: Request):
    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/commits"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        commits = r.json()[:10]  # limit to latest 10

    commit_data = [{
        "message": c["commit"]["message"],
        "author": c["commit"]["author"]["name"],
        "date": c["commit"]["author"]["date"],
        "url": c["html_url"]
    } for c in commits]

    return templates.TemplateResponse("logs.html", {
        "request": request,
        "commits": commit_data,
        "repo": f"{GITHUB_USER}/{GITHUB_REPO}"
    })
