from fastapi import status, Depends, HTTPException
from fastapi.routing import APIRouter
from .. import database, models, schemas
from sqlalchemy.orm import Session
from blog.repository import user

get_db = database.get_db

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/', status_code=201, response_model=schemas.User)
def create_user(request:schemas.BaseUser, db:Session=Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', status_code=200,response_model=schemas.ShowUser)
def show_user(id:int, db:Session=Depends(get_db)):
    return user.get(id, db)