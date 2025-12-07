from fastapi import FastAPI

app = FastAPI() #uvicorn app.main:app --reload to start the server

@app.get("/")
def root():
    return {"message" : "Study Assistant"}