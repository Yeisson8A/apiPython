from sqlalchemy.orm import Session
from models.models import Todo
from schemas.schemas import TodoSchema

def get_todos(db:Session):
    return db.query(Todo).all()

def get_todo_by_id(db:Session, id:int):
    return db.query(Todo).filter(Todo.id == id).first()

def create_todo(db:Session, todo:TodoSchema):
    _todo = Todo(text = todo.text, is_done = todo.is_done)
    db.add(_todo)
    db.commit()
    db.refresh(_todo)
    return _todo

def remove_todo(db:Session, id:int):
    _todo = get_todo_by_id(db=db,id=id)
    db.delete(_todo)
    db.commit()
    return _todo

def update_todo(db:Session, id:int, text:str, is_done:bool):
    _todo = get_todo_by_id(db=db, id=id)
    _todo.text = text
    _todo.is_done = is_done
    db.commit()
    db.refresh(_todo)
    return _todo