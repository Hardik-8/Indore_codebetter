from fastapi import FastAPI

app=FastAPI()

employees = [ {"id":1,"name":"rahul","salary":567890},

    {"id":2,"name":"rohit","salary":567244},
    {"id":3,"name":"amit","salary":567823}
    ]

@app.get("/")
def home():
    return {"message":"hello fastapi"}

@app.get("/employees")
def emplist():
    return employees


@app.get("/employees/{id}")
def employee(id:int):
    emp = None
    for e in employees:
        if e["id"] == id:
            emp = e
    if emp:
        return emp
    else :
        return {"message ": "not found2"}

@app.get("/employees/add")
def addemp(id : int,name : str,salary:int):
    newemp={"id":id,"name":name,"salary":salary}
    employees.append(newemp)
    return employees 

@app.get("/addemp")
def addemp(id : int,name : str,salary:int):
    newemp={"id":id,"name":name,"salary":salary}
    employees.append(newemp)
    return employees 


## add product ke liye post bhi banana hai 