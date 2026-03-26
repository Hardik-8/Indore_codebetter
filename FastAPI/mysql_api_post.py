from fastapi import FastAPI
import mysql.connector

class product:
    def __init__(self, id=0,name="",price=0):
        self.id=id
        self.name=name    
        self.price=price
    
mysqlcon=mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="PR")
app=FastAPI()

@app.get("/")
def home():
    return {"message":"hello CRUD API"}

@app.get("/products")
def products_list():
    query = "select * from products"
    cursor = mysqlcon.cursor() 
    cursor.execute(query)
    product_data=cursor.fetchall()
    products_list=[ ]
    for row in product_data:
        pro=product(
            id=row[0],name=row[1],price=row[2]
        )
        products_list.append(pro)
    return products_list    

@app.post("/products")
def addproduct(id:int,name:str,price:int):
    query="insert into products values (%s,%s,%s)"
    val=(id,name,price)
    cursor=mysqlcon.cursor()
    cursor.execute(query,val)
    mysqlcon.commit()
    cursor.close()
    return {"message":"new added "}


@app.get("/products/filter")
def filter_products(price:int):
    for i in products_list[2]:
        if price==price:
            return price
