from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from . import schema, model, hashing 


def create(req: schema.User, db: Session) -> model.User:
    new_user = model.User(
        username=req.username,
        email=req.email,
        password=hashing.Hasher.bcrypt(req.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_user(id: int, db: Session):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no user with id={id}')
    return user