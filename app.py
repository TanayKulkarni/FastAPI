from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="ui")

@app.get("/")
async def base():
    return {"Tanay": "Kulkarni"}

@app.get("/html",tags=['html'])
async def root():
    html_response = """
    <html>
        <head>
           <title>FastAPI</title>
        </head>
        <body><marquee>"""+'app bangaaya be!!!!'+"""</marquee>
        
        </body>
    </html>
    """

    return HTMLResponse(content=html_response,status_code=200)

# @app.get("/html_jinja/{id}",tags=['html'], response_class=HTMLResponse)
# async def example(request: Request, id:str):
#     return templates.TemplateResponse("index.html", {"request": request, 'id':id})

# @app.post("/login_inbuilt") ## yeh inbuilt fastapi ka form hai, post method jaisa hai 
# async def login(username: str = Form(...), password: str = Form(...)):
#     return {"username": username}

# @app.get("/form", response_class=HTMLResponse)
# async def form(request: Request):
#     return templates.TemplateResponse("form.html", {"request": request})

# @app.post("/login") ## yaaha html file ke form se values lega aur dekhega
# async def login(name: str = Form(...)):
#     return {"Username": name}