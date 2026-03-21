from fastapi import FastAPI

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

@app.get("/products/filter")
def filter_products(price:int):
    for i in products[2]:
        if price==price:
            return price

@app.get("/products/add_product")
def add_product(id :int,name : str ,price : int):
    new={"id":id,"name":name,"price":price}
    products.append(new)
    return products



