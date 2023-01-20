from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import schema
from .. import database
from . import usecase

router = APIRouter(prefix='/blog')

@router.post("/", response_model=schema.Blog)
def create_user(requset: schema.Blog, db: Session = Depends(database.get_db)):
    return usecase.create(requset, db)