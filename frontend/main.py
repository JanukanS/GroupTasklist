from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/",response_class = HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.get("/lobby/{room_id}",response_class = HTMLResponse)
async def room_lobby(request: Request, room_id:str):
    return templates.TemplateResponse("joinroom.html", {"request": request, "room_id": room_id})

@app.get("/room/{room_id}",response_class = HTMLResponse)
async def gen_room(request: Request, room_id:str):
    tasks = [0,0,0,0]
    tasks[0] = {
                "name":"Hackathon",
                "author":"Janukan",
                "starter":"Aaron",
                "finisher":"Jacob"
            }
    tasks[1] = {
                "name":"Do Homework",
                "author":"Janukan",
                "starter":"Janukan",
                "finisher":"Janukan"
                }
    tasks[2] = {
            "name":"unfinished",
            "author":"Janukan",
            "starter":"Janukan",
            "finisher":""
            }
    tasks[3] = {
            "name":"unstarted",
            "author":"Janukan",
            "starter":"",
            "finisher":""
            }

    return templates.TemplateResponse("taskroom.html",{"request":request, "room_id": room_id, "tasks": tasks})


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
