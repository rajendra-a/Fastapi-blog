from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title:str
    body:str
    user_id:int
    
class Blog(BaseModel):
    title:str
    body:str
    
    class Config:
        orm_mode = True

class BaseUser(BaseModel):
    name:str
    email:str
    password:str

    
class User(BaseModel):
    name:str
    email:str

    class Config:
        orm_mode = True
        
class ShowUser(User):
    blogs:List[Blog] = []

    class Config():
        orm_mode = True


class ShowBlog(Blog):
    creator:User

    class Config:
        orm_mode = True


class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
