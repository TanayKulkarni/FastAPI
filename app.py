from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def base():
    return {"Tanay": "Kulkarni"}

@app.get("/html",tags=['html'])
async def root():
    html_content = """
    <html>
        <head>
           <title>FastAPI</title>
        </head>
        <body><marquee>"""+'app bangaaya be!!!!'+"""</marquee>
        
        </body>
    </html>
    """

    return HTMLResponse(content=html_content,status_code=200)
