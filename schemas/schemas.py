from typing import Optional, TypeVar
from pydantic import BaseModel, field_validator

T = TypeVar("T")

class TodoSchema(BaseModel):
    id: Optional[int] = None
    text: str
    is_done: Optional[bool] = False

    @field_validator('text')
    def text_must_be_required(cls, v):
        if len(v) == 0:
            raise ValueError('Field "text" cannot be empty')
        return v
    
    class Config:
        orm_mode = True
        schema_extra  = {
            "example":
                {
                    "id": 0,
                    "text": "texto del todo",
                    "is_done": "todo completo o no"
                }
        }


class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T]