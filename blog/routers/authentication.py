from fastapi import status, HTTPException, APIRouter, Depends
from .. import schemas, models, database, token
from sqlalchemy.orm import Session
from ..hashing import hash
from datetime import timedelta

get_db = database.get_db

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:schemas.Login, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid credentials')
    if not hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'incorrect password')
   
    access_token = token.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

    return user


