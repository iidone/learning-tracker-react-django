from fastapi import FastAPI
from .database import engine
from .models import Base

app = FastAPI()

# Создание таблиц БД
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}