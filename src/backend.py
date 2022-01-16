from typing import Optional

from fastapi import FastAPI
from interfaceDB import *

app = FastAPI()
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
