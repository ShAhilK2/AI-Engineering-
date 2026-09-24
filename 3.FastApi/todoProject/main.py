
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# In-memory database
todos = []



# the app instance is the main component of our FastAPI application.
# it is used in configure the application

class Custom(BaseModel):
    name : str
    age : int

@app.get("/ping")
async def ping():
    return {"message": "Hello from FastAPI"}


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}



@app.get("/blogs/comments")
async def read_blog_comments():
    return {"comments": "No Comments yet"}

@app.get("/blogs/{blogsId}")
async def blogs(blogsId: int,name:str =None,surname:str=None):
    return {"message": f"Welcome to the blogs page! Blog ID: {blogsId}", "Name": name + " " + surname}



@app.post("/user")
async def createUser(request_body : Custom):
    print(request_body.name)
    return {"user" : request_body}


# Sending Data via req body



class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


@app.get("/")
def root():
    return {"message": "Welcome to Todo Backend By FastAPI"}


# GET all todos
@app.get("/todos")
def get_todos():
    return todos


# GET todo by ID
@app.get("/todos/{todo_id}")
def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo

    return {"error": "Todo by that id not found"}


# CREATE todo
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo.dict())
    return todos[-1]


# DELETE todo
@app.delete("/todos/{todo_id}")
def delete_todo_by_id(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted"}

    return {"error": "Todo by that id not found"}


# PUT => update entire resource
@app.put("/todos/{todo_id}")
def update_todo_by_id(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos[index] = updated_todo.dict()
            return {
                "message": "Todo updated",
                "todo": todos[index]
            }

    return {"error": "Todo by that id not found"}


# PATCH => update specific fields
@app.patch("/todos/{todo_id}")
def patch_todo_by_id(todo_id: int, updated_todo: Todo):
    for todo in todos:
        if todo["id"] == todo_id:
            todo.update(updated_todo.dict())

            return {
                "message": "Todo updated",
                "todo": todo
            }

    return {"error": "Todo by that id not found"}





