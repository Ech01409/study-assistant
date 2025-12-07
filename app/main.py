from fastapi import FastAPI
from app.api.summarize import router as summarize_router

app = FastAPI() #uvicorn app.main:app --reload to start the server

app.include_router(
    summarize_router,
    prefix="/api",
    tags=["Summarization"]
)

@app.get("/")
def root():
    return {"message" : "Study Assistant"}