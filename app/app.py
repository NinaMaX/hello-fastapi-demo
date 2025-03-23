from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

@app.post("/health/")
async def health_check():
    return {"status": "UP", "message": "Service is running"}

class EchoSchema(BaseModel):
    message: str

@app.post("/echo/")
async def echo(request: EchoSchema):
    return {"message": request.message}

# File upload endpoint
def check_file_type(file: UploadFile) -> dict:
    """
    Check the type of the uploaded file and return relevant information.
    """
    file_type_info = {
        "filename": file.filename,
        "content_type": file.content_type
    }

    # Check if the file is an MP3
    if file.content_type == "audio/mpeg":
        file_type_info["message"] = "This is an MP3 file."
    else:
        file_type_info["message"] = "This is not an MP3 file."
    
    return file_type_info

async def load_file(file: UploadFile = File(...)) -> dict:
    """
    Load a file from the request and check its validity.
    """
    if not file:
        raise HTTPException(status_code=400, detail="No file provided")
    
    file_info = check_file_type(file)
    return file_info

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    """
    Endpoint to handle file uploads and determine file type.
    """
    file_info = await load_file(file)
    return file_info