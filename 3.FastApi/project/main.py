from fastapi import FastAPI,Depends
from models import TodoModel
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional,List

app=FastAPI() # create an instance of FastAPI

# Creete the table in the database
TodoModel.metadata.create_all(bind=engine)


class TodoBase(BaseModel):
    title :str
    description : Optional[str] =None
    completed : bool = False

class TodoCreate(TodoBase):
    pass
class TodoUpdate(TodoBase):
    pass
class TodoResponse(TodoBase):
    id:int

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        # yield is like return but it allows the function to continue after the yield   
        yield db
    finally:
        db.close()
    


@app.get("/todos",response_model = List[TodoResponse])
def getAllTodos(db : Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos    




@app.get("/todos/{todo_id}",response_model = TodoResponse)
def getTodoById(todo_id : int,db : Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    return todo



@app.post("/todos",response_model = TodoResponse)
def create_todo(todo : TodoBase,db :Session = Depends(get_db) ):
    # Create a new todo object
    db_todo = TodoModel(title = todo.title,description = todo.description,completed = todo.completed)
    # add the todo to the database
    db.add(db_todo)
    # commit the transaction
    db.commit()
    # refresh the todo to get the id
    db.refresh(db_todo)

    return db_todo




@app.delete("/todos/{todo_id}")
def deleteTodoById(todo_id : int,db : Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    db.delete(todo)
    #  db.commit()
    db.commit() # Commit the transaction
    return todo


# PUT replaces the whole resource — every field is overwritten
@app.put("/todos/{todo_id}", response_model=TodoResponse)
def updateTodoById(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    # PUT replaces the whole resource — every field is overwritten
    db_todo.title = todo.title
    db_todo.description = todo.description
    db_todo.completed = todo.completed

    db.commit()
    db.refresh(db_todo)
    return db_todo



class TodoPatch(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
# Update Specific Field
@app.patch("/todos/{todo_id}", response_model=TodoResponse)
def updateSpecificFieldbyId(todo_id: int, todo: TodoPatch, db: Session = Depends(get_db)):
    db_todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    update_data = todo.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo


