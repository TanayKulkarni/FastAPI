from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def base():
    return {"Tanay": "Kulkarni"}

@app.get("/html",tags=['html'])
async def root():
    return HTMLResponse(content='index.html',status_code=200)
