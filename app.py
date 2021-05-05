from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from iris import ml
from urllib.parse import urljoin

app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")

templates = Jinja2Templates(directory="ui")

@app.get("/")
async def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})



@app.post("/iris",response_class=HTMLResponse) ## yaaha html file ke form se values lega aur dekhega
async def login(request: Request, w: int = Form(...),x: int = Form(...),y: int = Form(...),z: int = Form(...)):
    flower =  ml(int(w),int(x),int(y),int(z))
    img_url = 'images/'+ flower + '.jpg'
    # html_response = """
    # <!DOCTYPE html>
    # <html>
    #     <head>
    #        <title>FastAPI</title>
    #     </head>
    #     <body background ="""+img_url+""">
    #         <b><strong><h1 style="text-align:center;color:white">
    #         """+flower+"""</h1></b></strong>
    #     </body>
    # </html>
    # """

    # return HTMLResponse(content=html_response,status_code=200)
    return templates.TemplateResponse("image.html", {"request": request, "img_url":img_url,'flower':flower})
    # return FileResponse(img_url)

@app.get("/im",response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("image.html", {"request": request})

