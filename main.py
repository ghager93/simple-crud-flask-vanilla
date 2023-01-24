from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

engine = create_engine("sqlite:///app.db")

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Test(Base):
    __tablename__ = "test"

    test = Column(Integer, primary_key=True)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World!"}