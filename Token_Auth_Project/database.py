from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL="mysql+pymysql://root:0000@localhost:3306/token_Auth_db"
engine=create_engine(DATABASE_URL)

Session_local=sessionmaker(autocommit=False,autoflush=False,bind=engine)
BASE=declarative_base()

def get_db():
    db=Session_local()
    try:
        yield db
    finally:
        db.close






