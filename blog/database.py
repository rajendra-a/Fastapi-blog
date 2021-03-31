# import os, urllib
"""Use this when you want to get the from other parts"""

# Import SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# host_server = os.environ.get('host_server', 'localhost')
# db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
# database_name = os.environ.get('database_name', 'rajendra')
# db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'rajendra')))
# db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'rajendra')))
# ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
# DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
SQLALCHEMY_DATABASE_URL = "postgresql://rajendra:rajendra@localhost/rajendra"


# In this example we are connecting to sqlite database
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# The sessionmaker create a session for database with the following conditions
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Database Base system which maps with the pydantic schema 
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()









