from fastapi import FastAPI,Form 
import math
from typing import Annotated
from fastapi.responses import HTMLResponse
app=FastAPI()

@app.get("/")
def home():
    return { "message" : "hello FastAPI"}
    
@app.post("/square")
def square(num:Annotated[int , Form()]):
    return {"sqaure ": num*num}  


@app.post("/voter")
def voter(name :Annotated[str , Form()] , age:Annotated[int , Form()]):
    if age>=18:
        return {"message":"eligible for vote"}
    else:
        return {"message":"not eligible for vote"}
    
@app.post("/percentage")
def percentage(rollno:Annotated[float , Form()] ,hindi: Annotated[float , Form()] ,english:Annotated[float , Form()] ,maths:Annotated[float , Form()],science:Annotated[float , Form()]):
    c=hindi+english+maths+science
    tot=400
    d=(c/tot)*100
    return { "percentage" : d }
        
    
    