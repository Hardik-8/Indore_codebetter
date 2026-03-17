from fastapi import FastAPI
import math
from fastapi.responses import HTMLResponse
app=FastAPI()

@app.get("/")
def home():
    return { "message" : "hello FastAPI"}
    
@app.get("/square")
def square(num:int):
    return {"sqaure ": num*num}  


@app.get("/voter")
def voter(name :str , age:int):
    if age>=18:
        return {"message":"eligible for vote"}
    else:
        return {"message":"not eligible for vote"}
    
@app.get("/percentage")
def percentage(rollno:float ,hindi: float ,english:float ,maths:float,science:float):
    c=hindi+english+maths+science
    tot=400
    d=(c/tot)*100
    return { "percentage" : d }
        
    
    