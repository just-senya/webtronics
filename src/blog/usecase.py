from sqlalchemy.orm import Session

from . import schema, model

def create(req: schema.Blog, db: Session):
    new_blog = model.Blog(
        title=req.title,
        content=req.content
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog