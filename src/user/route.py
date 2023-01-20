from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import schema
from . import usecase
from .. import database

router = APIRouter(prefix='/user')

@router.post("/", response_model=schema.GetUser)
def create_user(request: schema.User, db: Session = Depends(database.get_db)):
    return usecase.create(request, db)

@router.get("/{id}", response_model=schema.GetUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return usecase.get_user(id, db)