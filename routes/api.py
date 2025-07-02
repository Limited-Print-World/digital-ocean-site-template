import os
import time
from fastapi import APIRouter, Form
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse

router = APIRouter()

@router.get("/file")
async def get_file():
    file_path = "static/example.txt"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="text/plain")
    return JSONResponse(content={"error": "File not found"}, status_code=404)

@router.get("/json")
async def get_json():
    return {"message": "This is a JSON response", "status": "success"}

@router.get("/stream")
async def stream_response():
    def generate():
        for i in range(5):
            yield f"Chunk {i}\n"
            time.sleep(1)
    return StreamingResponse(generate(), media_type="text/plain")

@router.post("/call-api")
async def call_api(payload: str = Form(...)):
    return {"status": "received", "input": payload}
