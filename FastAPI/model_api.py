from fastapi import FastAPI

app=FastAPI()


class employee:
    def __init__(self,id=0,name="",salary=0):
        self.id=id
        self.name=name
        self.salary=salary

e1=employee(id=101,name="amit",salary=20987)
e2=employee(id=102,name="rahul",salary=90976)
e3=employee(id=103,name="suresh",salary=60976)
e4=employee(id=104,name="ramesh",salary=80000)
e5=employee(id=105,name="mahesh",salary=40986)
e6=employee(id=106,name="ramU",salary=50976)

employees = [e1,e2,e3,e4,e5,e6]


@app.get("/")
def home():
    return {"message":"hello fastapi"}

@app.get("/employees")
def emplist():
    return employees


@app.post("/employees/add")
def addemp(id : int,name : str,salary:int):
    newemp=employee(id=id,name=name,salary=salary)
    employees.append(newemp)
    return employees 

@app.get("/employees/add")
def addemp(id : int,name : str,salary:int):
    newemp=employee(id=id,name=name,salary=salary)
    employees.append(newemp)
    return employees 


@app.get("/employees/get/{id}")
def get_employee(id:int):
    emp = None
    for e in employees:
        if e.id == id:
            emp = e
    if emp:
        return emp
    else :
        return {"message ": "not found2"}
    
@app.delete("/employee/{id}")
def delete_emp(id:int):
    for e in employees:
        if e.id==id:
            employees.remove(e)
    return employees

# @app.put("/addemp")
# def updateemp(id : int,name : str,salary:int):
#     newemp=employee(id=id,name=name,salary=salary)
#     employees.append(newemp)
#     return employees

@app.put("/employee")
def updateemp(id : int,name : str,salary:int):
    for e in employees:
        if e.id == id:
            e.name = name
            e.salary = salary
    return employees 




