
from os import name
from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from .hashing import bcrypt



app = FastAPI()

# When ever find new models let's create it on database
models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()


@app.post('/blog', status_code=201, tags=['blogs'])
def create(request:schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}', status_code=204, tags=['blogs'])
def delete(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not available")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put('/blog/{id}', status_code=202, tags=['blogs'])
def destroy(id, request:schemas.Blog, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")

    blog.update(request)
    db.commit()
    return 'updated'

@app.get('/blog', status_code=200, response_model=List[schemas.ShowBlog], tags=['blogs'])
def get_all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
def show(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not available")
    return blog

@app.post('/user', status_code=201, response_model=schemas.ShowUser,tags=['users'] )
def create_user(request:schemas.User, db:Session=Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{id}', status_code=200,response_model=schemas.ShowUser, tags=['users'])
def show_user(id:int, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    return user
