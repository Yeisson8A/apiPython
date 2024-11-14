from fastapi import FastAPI
import uvicorn
import models.models as model
from db.config import engine
from routes.routes import router as router_crud

model.Base.metadata.create_all(engine)

app = FastAPI(
    title="Todo API",
    description="Operaciones CRUD usando una API",
    version="1.0.0"
)

app.include_router(router=router_crud,tags=["CRUD"],prefix="/todo")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True)