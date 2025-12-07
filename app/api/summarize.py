from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends, APIRouter 
import shutil
import os
import tempfile

router = APIRouter()

@router.post("/pdf")
async def summarize_pdf(file: UploadFile = File(...)):
    if file:
        return {"message" : "file recieved"}

