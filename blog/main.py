from fastapi import FastAPI
from . import models
from .database import engine
from blog.routers import blog, user, authentication


app = FastAPI()

# When ever find new models let's create it on database
models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)












