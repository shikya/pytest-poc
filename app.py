from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv
import os

# ----------------------
# LOAD ENV
# ----------------------
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in .env")


# ----------------------
# DB CONFIG
# ----------------------
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# ----------------------
# MODEL
# ----------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


# ----------------------
# CREATE TABLE (TEMP ONLY)
# ----------------------
Base.metadata.create_all(bind=engine)


# ----------------------
# FASTAPI APP
# ----------------------
app = FastAPI()


# ----------------------
# DB DEPENDENCY
# ----------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------
# API ENDPOINT
# ----------------------
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users