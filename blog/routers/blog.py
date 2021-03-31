from typing import List
from fastapi import status, Depends, HTTPException, APIRouter
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..repository import blog
get_db = database.get_db

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/', status_code=200, response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(get_db)):
    return blog.get_all(db)

@router.post('/', status_code=201, response_model=schemas.Blog)
def create(request:schemas.BlogBase, db:Session = Depends(get_db)):
    return blog.post(request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, db:Session = Depends(get_db)):
    return blog.get(id, db)

@router.put('/{id}', status_code=202)
def update(id, request:schemas.Blog, db:Session = Depends(get_db)):
    return blog.update(id, request, db)

@router.delete('/{id}', status_code=204)
def destroy(id, db:Session = Depends(get_db)):
    return blog.destroy(id, db)




