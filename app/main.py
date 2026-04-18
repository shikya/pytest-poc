from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()

from .db import engine, Base
from .models import User
from .deps import get_db

app = FastAPI()

# TEMP: create tables (remove after Alembic)
# Base.metadata.create_all(bind=engine)


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()