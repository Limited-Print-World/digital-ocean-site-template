
import os,sys,time,json
from pathlib import Path


from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

# https://documentation.bloomreach.com/engagement/docs/datastructures
from routes import html, api, dev, forms  # ⬅ add dev


root = Path(os.path.dirname( __file__ ))

static_dir = root/'static'
static_css = static_dir/'styles.css'
static_js = static_dir/'main.js'
static_img_dir = static_dir/'img'

static_templates = root/'templates'



class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            html = open(root/'static/index.html').read()
            self.wfile.write(html.encode())

        elif self.path == "/file":
            file_path = "static/example.txt"
            if os.path.exists(file_path):
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(HTTPStatus.NOT_FOUND, "File not found")

        elif self.path == "/json":
            data = {"message": "This is a JSON response", "status": "success"}
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/stream":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Transfer-Encoding", "chunked")
            self.end_headers()

            for i in range(5):
                chunk = f"Chunk {i}\n".encode()
                self.wfile.write(chunk)
                self.wfile.flush()
                time.sleep(1)

        else:
            self.send_error(HTTPStatus.NOT_FOUND, "Route not found")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        fields = parse_qs(post_data.decode())

        if self.path == "/submit-email":
            email = fields.get("email", [""])[0]
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            response = f"<html><body><h2>Email submitted: {email}</h2></body></html>"
            self.wfile.write(response.encode())

        elif self.path == "/call-api":
            payload = fields.get("payload", [""])[0]
            # Here you'd handle or simulate an API call
            result = f"Received API payload: {payload}"
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "received", "input": payload}).encode())

        else:
            self.send_error(HTTPStatus.NOT_FOUND, "POST route not found")

# Make sure the static file exists
os.makedirs("static", exist_ok=True)
with open("static/example.txt", "w") as f:
    f.write("This is an example file.")


app = FastAPI()

# Serve raw static HTML files from public/
app.mount("/templates", StaticFiles(directory=static_templates), name="templates")
# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory=static_dir), name="static")
resources = Jinja2Templates(directory=static_dir)

@app.get("/static/{path:path}")
async def custom_static(path: str):
    return FileResponse(
        f"static/{path}",
        # keeps cache fresh for easier client side updates during hot dev times.
        headers={"Cache-Control": "no-cache, no-store, must-revalidate"}
    )

@app.get("/favicon.ico", response_class=FileResponse)
def get_favicon():
    '''adds a favicon to the title.'''
    return FileResponse(static_dir/"img/favicon.ico")
# @app.get("/img/favicon.ico", response_class=FileResponse)
# def get_favicon(request: Request):
#     '''adds a favicon to the title.'''
#     return resources.TemplateResponse(root/"static/img/favicon.ico")
@app.get("/img/raven_head_left.png", response_class=FileResponse)
def get_favicon():
    '''adds a favicon to the title.'''
    return FileResponse("/img/raven_head_left.png")
@app.get("/css/styles.css", response_class=FileResponse)
def get_favicon(request: Request):
    '''adds a favicon to the title.'''
    return resources.TemplateResponse("/css/styles.css")
@app.get("/css/vars.css", response_class=FileResponse)
def get_favicon(request: Request):
    '''adds a favicon to the title.'''
    return resources.TemplateResponse("/css/vars.css")


# Mount routers
app.include_router(html.router)
app.include_router(html.forms_router)
app.include_router(api.router)
app.include_router(dev.router)

# Attach Jinja template directory
templates = Jinja2Templates(directory="templates")