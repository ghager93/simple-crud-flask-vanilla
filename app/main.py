from typing import Optional

from fastapi import FastAPI
# from sqlalchemy import create_engine, Column, Integer
# from sqlalchemy.orm import sessionmaker, declarative_base

from sqlmodel import SQLModel, Field, create_engine, Session


app = FastAPI()

engine = create_engine("sqlite:///app.db")

# SessionLocal = sessionmaker(bind=engine)

# Base = declarative_base()

# class Test(Base):
#     __tablename__ = "test"

#     test = Column(Integer, primary_key=True)


class Test2(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    test: int
    string: str = Field(default="") 

# Base.metadata.create_all(bind=engine)
SQLModel.metadata.create_all(engine)

@app.get("/")
async def root():
    with Session(engine) as session:
        session.add(Test2(test="hi"))
        session.commit()
    return {"message": "Hello World!"}