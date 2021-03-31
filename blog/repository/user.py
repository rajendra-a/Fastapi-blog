from fastapi import HTTPException, status
from .. import models, schemas, hashing
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def create(request:schemas.BaseUser, db:Session):
    new_user = models.User(name=request.name, email=request.email, password=hashing.hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    return user
