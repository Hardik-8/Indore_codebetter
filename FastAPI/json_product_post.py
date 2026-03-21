from fastapi import FastAPI , Form
from typing import Annotated
import math

app=FastAPI()

@app.get("/")
def home():
    return {"message":"hello fastapi"}

products=[
    {"id":1,"name":"laptop","price":123456},
    {"id":2,"name":"mobile","price":234345},
    {"id":3,"name":"tablet","price":987436}
]
@app.get("/products")
def get_products():
    return products

@app.post("/products/filter")
def filter_products(price:Annotated[int , Form()]):
    return price

@app.post("/products/add_product")
def add_product(id :Annotated[int , Form()],name : Annotated[str , Form()] ,price : Annotated[int , Form()]):
    new={"id":id,"name":name,"price":price}
    products.append(new)
    return products



