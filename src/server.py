from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from interfaceDB import *
from os import environ
from time import sleep

app = FastAPI()
templates = Jinja2Templates(directory="templates")
sleep(10)
a_connect()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

#Data API endpoints
@app.get('/clear')
async def clear_db():
    a_connect()
    return True

@app.get('/create-room')
async def create_room():
    return b_create_room()

@app.get('/create-task/{room_id}/{title}/{authour}')
async def create_task(title, authour, room_id):
    await manager.broadcast("refresh please")
    c_create_task(title,authour,room_id)
    return True

@app.get('/task_table/{room_id}')
async def task_table(room_id):
    return f_retrieve(room_id)

@app.get('/start_task/{room_id}/{task_id}/{person}')
async def start_task(task_id,person,room_id):
    await manager.broadcast("refresh please")
    return d_start_task(task_id,person,room_id)

@app.get('/finish_task/{room_id}/{task_id}/{person}')
async def finish_task(task_id,person,room_id):
    await manager.broadcast("refresh please")
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
    return templates.TemplateResponse("taskroom.html",{
        "request":request,
        "room_id": room_id,
        "username":username, 
        "tasks": taskdata,
        "urlpath": environ.get('PROJECT_URL')
        })

#Websockets
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
@app.get("/refresh")
async def send_refresh():
    await manager.broadcast("refresh please")
    return True

