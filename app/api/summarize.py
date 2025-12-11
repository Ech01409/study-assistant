from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends, APIRouter 
import shutil
import os
import uuid
import tempfile
from app.services.pdf_summary import extract_txt_from_pdf

router = APIRouter()

@router.post("/pdf")
async def summarize_pdf(file: UploadFile = File(...)):
    temp_file_path = None
    try:
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            temp_file_path = temp_file.name
            shutil.copyfileobj(file.file, temp_file)

        text = extract_txt_from_pdf(temp_file_path) 
        return {"extracted text" : text[:500]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.remove(temp_file_path)    
        file.file.close()    
          


