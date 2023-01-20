from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str


class GetUser(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True