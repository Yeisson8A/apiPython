from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from db import crud
from db.config import get_db
from schemas.schemas import Response, TodoSchema
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/")
async def create_todo_service(request: TodoSchema, db: Session = Depends(get_db)):
    crud.create_todo(db, todo=request)
    return Response(status="Ok", code="200", message="Todo created successfully",result=jsonable_encoder(request)).model_dump(exclude_none=True)

@router.get("/")
async def get_todos(db: Session = Depends(get_db)):
    _todos = crud.get_todos(db)
    return Response(status="Ok", code="200", message="Success fetch all data", result=jsonable_encoder(_todos))

@router.get("/{id}")
async def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    _todo = crud.get_todo_by_id(db, id=id)
    return Response(status="Ok", code="200", message="Success fetch data", result=jsonable_encoder(_todo))

@router.put("/{id}")
async def update_todo(id: int, request: TodoSchema, db: Session = Depends(get_db)):
    try:
        _todo = crud.update_todo(db, id=id, text=request.text, is_done=request.is_done)
        return Response(status="Ok", code="200", message="Todo updated successfully", result=jsonable_encoder(_todo))
    except Exception as e:
        return Response(
            status="bad",
            code="304",
            message="the updated gone wrong"
        )


@router.delete("/{id}")
async def delete_todo(id: int, db: Session = Depends(get_db)):
    try:
        _todo = crud.remove_todo(db, id=id)
        return Response(status="Ok", code="200", message="Todo deleted successfully", result=None).model_dump(exclude_none=True)
    except Exception as e:
        return Response(
            status="bad",
            code="",
            message="the deleted gone wrong"
        )