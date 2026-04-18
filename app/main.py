from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from .schemas import UserResponse, UserCreate

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

# from fastapi import HTTPException
# from sqlalchemy.exc import IntegrityError
#
@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already exists")

    return db_user