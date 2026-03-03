from fastapi import FastAPI
from utils import add_numbers

app=FastAPI()

@app.get("/")
def home():
    return {"message":"FastAPI CI/CD working!"}

@app.get("/add/{a}/{b}")
def add(a:int,b:int):
    result=add_numbers(a,b)
    return {"result":result}