from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

@app.get("/")
def home():
    return "hello world"

@app.get("/mydata",response_class=HTMLResponse)
def mydata():
    return """<html>
                <head>
        <title>
            demo file html 2 
        </title>

    </head>
    <body>
        <center><h1> LOGIN FROM</h1> </center>
        <center > 
            <form action="" method="post">
            Name:
            <input type="text" id="name" name="name" value="xyz">
            <input type="text" id="name" name="name" placeholder="enter you name" required>
            <input type="text" id="name" name="name" hidden><br><hr>
            Message
            <textarea placeholder="enter the text"></textarea><br><br>
            
            gender:
            <select id="gender" name="gender">
                <option value="male"> male</option>
                <option value="female"> female</option>
                <option value="other"> other  </option>
            </select>

            <input type="submit" value="save">
                 

            
        </form>
        </center>
    </body>
</html>"""


@app.get("/factorial/{data}")
def factorial(data : int):
    n=data
    f=1
    for i in range(1,n+1):
        f=f*i
    return {"factorial " : f}

@app.get("/voter")
def voter(name :str,age:int):
    if age>=18:
        return {"message":"eligible for vote"}
    else:
        return {"message":"not eligible for vote"}
    
@app.get("/max")
def max(a:int,b:int,c:int):
    if(a>b and a>c):
        print("a is the greatest number")
    if(b>a and b>c):
        print("b is the greatest number")
    else:
        print("c is the greatest number")

