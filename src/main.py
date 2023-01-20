from fastapi import FastAPI
from pydantic import BaseModel

from . import database

from .user import route as userRoute
from .blog import route as blogRoute
from .auth import route as authRoute
from .user import model

app = FastAPI()

app.include_router(blogRoute.router)
app.include_router(userRoute.router)
app.include_router(authRoute.router)

model.MyBase.metadata.create_all(database.engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

