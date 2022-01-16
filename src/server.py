from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from interfaceDB import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")

#Data API endpoints
@app.get('/clear')
def clear_db():
    a_connect()
    return True

@app.get('/create-room')
def create_room():
    return b_create_room()

@app.get('/create-task/{room_id}/{title}/{authour}')
def create_task(title, authour, room_id):
    c_create_task(title,authour,room_id)
    return True

@app.get('/task_table/{room_id}')
def task_table(room_id):
    return f_retrieve(room_id)

@app.get('/start_task/{room_id}/{task_id}/{person}')
def start_task(task_id,person,room_id):
    return d_start_task(task_id,person,room_id)

@app.get('/finish_task/{room_id}/{task_id}/{person}')
def finish_task(task_id,person,room_id):
    return e_complete(task_id,person,room_id)

#HTML API endpoints
@app.get("/",response_class = HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.get("/lobby/{room_id}",response_class = HTMLResponse)
async def room_lobby(request: Request, room_id:str):
    return templates.TemplateResponse("joinroom.html", {"request": request, "room_id": room_id})

@app.get("/room/{room_id}/{username}",response_class = HTMLResponse)
async def gen_room(request: Request, room_id:str,username:str):
    taskdata = f_retrieve(room_id)
    for index,tupleVal in enumerate(taskdata):
        taskdata[index] = list(tupleVal)
        for index2,value in enumerate(taskdata[index]):
            taskdata[index][index2] = '' if value is None else value
    return templates.TemplateResponse("taskroom.html",{"request":request, "room_id": room_id,"username":username, "tasks": taskdata})


