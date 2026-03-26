from fastapi import FastAPI
import mysql.connector

class employee:
    def __init__(self, empid=0,firstname="",lastname="",email="",phone="",gender="",salary=0):
        self.empid=empid
        self.firstname=firstname    
        self.lastname=lastname
        self.email=email
        self.phone=phone
        self.gender=gender
        self.salary=salary

mysqlcon=mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="fastapi"
)

app=FastAPI()

@app.get("/")
def home():
    return {"message":"hello CRUD API"} # Read mtlb ki get krna 

@app.get("/employee")
def employee_list():
    query = "select * from employee"
    cursor = mysqlcon.cursor() 
    cursor.execute(query)
    empdata=cursor.fetchall()
    empdata_list=[ ]
    for row in empdata:
        emp=employee(
            empid=row[0],firstname=row[1],lastname=row[2],email=row[3],phone=row[4],gender=row[5],salary=row[6]
        )
        empdata_list.append(emp)
    return empdata_list

@app.post("/employee")
def addemp(empid:int,firstname:str,lastname:str,email:str,phone:str,gender:str,salary:int):
    query="insert into employee values (%s,%s,%s,%s,%s,%s,%s)"
    val=(empid,firstname,lastname,email,phone,gender,salary)
    cursor=mysqlcon.cursor()
    cursor.execute(query,val)
    mysqlcon.commit()
    cursor.close()
    return {"message":"new added "}

@app.post("/employee")
def delete(empid:int):
    query="delete from employee where empid=%s"
    val=(empid)
    cursor=mysqlcon.cursor()
    cursor.execute(query,val)
    mysqlcon.commit()
    cursor.close()
    return {"message":"new added"}

# product table 

