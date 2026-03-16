from fastapi import FastAPI
import math
app=FastAPI()

#/math/cube/7 , /math/factorical
@app.get("/math/{operation}/{num}")
def calculate(operation:str,num:int):
    if operation=='cube':
        return{"cube",num**3}
    elif operation =='square':
        return {"square":num**2}
    elif operation=='factorial':
        return {"factorial",math.factorial(num)}
    

@app.get("/items/{item_id}/")
def read_item(item_id:str,q:str | None = None ):
    if q:
        return{"item_id":item_id,"q":q}
    return{"item_id":item_id}              
    

@app.get("/discount")
def diss(amount:int,married:bool):
    if married:
        return {"discount": amount*0.1}
    else:
        return{"discount": amount*0.2}
    