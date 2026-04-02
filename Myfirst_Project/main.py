#main.py
from database import BASE,engine,Session,get_db
from fastapi import FastAPI,Depends,HTTPException
from schemas import Employee_create,Employee_Show,Student_create,Student_Show,Category_Create,Category_Show,Product_Create,Product_Show
from typing import List
from model import Employee,Student,Category,Product
app=FastAPI()
BASE.metadata.create_all(bind=engine)

@app.get("/")
def hello():
    return {"hello ":"database connection succesfull"}

@app.get("/emp_show",response_model=List[Employee_Show])
def employee_show(db:Session=Depends(get_db)):
    rec=db.query(Employee).all()
    # print("no pydantic class",rec)
    return rec 

@app.post("/emp_create",response_model=Employee_Show)
def employee_create(emp_data:Employee_create,db:Session=Depends(get_db)):
    emp_rec=Employee(**emp_data.dict())   #ye dictionary unpack kr rha hai dynamically krna hota hai 
    db.add(emp_rec)
    db.commit()
    db.refresh(emp_rec)
    # print("json",emp_rec)
    return emp_rec

@app.get("/emp_filter/{empid}/",response_model=Employee_Show)
def employee_single_rec(empid:int,db:Session=Depends(get_db)):
    emp_rec=db.query(Employee).filter(Employee.empid==empid).first()
    if emp_rec is None:
        raise HTTPException(status_code=404,detail="employee not found")
    return emp_rec

@app.put("/emp_update/{empid}/",response_model=Employee_Show)
def employee_update(empid:int,emp_upd:Employee_create,db:Session=Depends(get_db)):
    emp_rec=db.query(Employee).filter(Employee.empid==empid).first()
    if emp_rec is None:
        raise HTTPException(status_code=404,detail="employee not found")
    emp_rec.empid==empid
    emp_rec.name=emp_upd.name
    emp_rec.age=emp_upd.age
    emp_rec.salary=emp_upd.salary
    emp_rec.city=emp_upd.city
    db.commit()
    db.refresh(emp_rec)
    return emp_rec
    

@app.delete("/emp_delete/{empid}/")
def employee_delete(empid:int,db:Session=Depends(get_db)):
    emp_rec=db.query(Employee).filter(Employee.empid==empid).first()
    if emp_rec is None:
        raise HTTPException(status_code=404,detail="employee not found")
    db.delete(emp_rec)
    db.commit()
    # db.refresh(emp_rec)
    return {'msg':'employee deleted succesfully'}

#-----------------------------------------------------------------------------------------------------------------------]

@app.get("/student_show",response_model=List[Student_Show])
def Student_show(db:Session=Depends(get_db)):
    rec=db.query(Student).all()
    # print("no pydantic class",rec)
    return rec

@app.post("/std_create",response_model=Student_Show)
def student_create(stu_data:Student_create,db:Session=Depends(get_db)):
    emp_rec=Student(**stu_data.dict())   #ye dictionary unpack kr rha hai dynamically krna hota hai 
    db.add(emp_rec)
    db.commit()
    db.refresh(emp_rec)
    # print("json",emp_rec)
    return emp_rec

@app.get("/std_filter/{roll_no}/",response_model=Student_Show)
def student_single_rec(roll_no:int,db:Session=Depends(get_db)):
    std_rec=db.query(Student).filter(Student.roll_no==roll_no).first()
    if std_rec is None:
        raise HTTPException(status_code=404,detail="student not found")
    return std_rec

@app.put("/std_update/{roll_no}/",response_model=Student_Show)
def student_update(roll_no:int,std_upd:Student_create,db:Session=Depends(get_db)):
    std_rec=db.query(Student).filter(Student.roll_no==roll_no).first()
    if std_rec is None:
        raise HTTPException(status_code=404,detail="student not found")
    std_rec.roll_no==roll_no
    std_rec.name=std_upd.name
    std_rec.course=std_upd.course
    std_rec.fees=std_upd.fees
    db.commit()
    db.refresh(std_rec)
    return std_rec


@app.delete("/std_delete/{roll_no}/")
def student_delete(roll_no:int,db:Session=Depends(get_db)):
    std_rec=db.query(Student).filter(Student.roll_no==roll_no).first()
    if std_rec is None:
        raise HTTPException(status_code=404,detail="student not found")
    db.delete(std_rec)
    db.commit()
    # db.refresh(emp_rec)
    return {'msg':'student deleted succesfully'}


#------------------------------------------------------------------------------------------------------------------------]

@app.get("/Category_show",response_model=List[Category_Show])
def Category_show(db:Session=Depends(get_db)):
    rec=db.query(Category).all()
    # print("no pydantic class",rec)
    return rec

@app.post("/Cat_create",response_model=Category_Show)
def Category_create(cat_data:Category_Create,db:Session=Depends(get_db)):
    emp_rec=Category(**cat_data.dict())   #ye dictionary unpack kr rha hai dynamically krna hota hai 
    db.add(emp_rec)
    db.commit()
    db.refresh(emp_rec)
    # print("json",emp_rec)
    return emp_rec

@app.get("/Cat_filter/{cat_id}/",response_model=Category_Show)
def Category_single_rec(cat_id:int,db:Session=Depends(get_db)):
    std_rec=db.query(Category).filter(Category.cat_id==cat_id).first()
    if std_rec is None:
        raise HTTPException(status_code=404,detail="student not found")
    return std_rec

@app.put("/cat_update/{roll_no}/",response_model=Category_Show)
def category_update(cat_id:int,cat_upd:Category_Create,db:Session=Depends(get_db)):
    std_rec=db.query(Category).filter(Category.cat_id==cat_id).first()
    if std_rec is None:
        raise HTTPException(status_code=404,detail="student not found")
    std_rec.cat_id==cat_id
    std_rec.cat_name=cat_upd.cat_name

    db.commit()
    db.refresh(std_rec)
    return std_rec

@app.delete("/cat_delete/{cat_id}/")
def category_delete(cat_id:int,db:Session=Depends(get_db)):
    emp_rec=db.query(Category).filter(Category.cat_id==cat_id).first()
    if emp_rec is None:
        raise HTTPException(status_code=404,detail="employee not found")
    db.delete(emp_rec)
    db.commit()
    # db.refresh(emp_rec)
    return {'msg':'category deleted succesfully'}


#---------------------------------------------------------------------------------------------------------------------]

@app.get("/Product_show",response_model=List[Product_Show])
def Product_show(db:Session=Depends(get_db)):
    rec=db.query(Product).all()
    # print("no pydantic class",rec)
    return rec

@app.post("/pd_create",response_model=Product_Show)
def Product_create(pd_data:Product_Create,db:Session=Depends(get_db)):
    emp_rec=Product(**pd_data.dict())   #ye dictionary unpack kr rha hai dynamically krna hota hai 
    db.add(emp_rec)
    db.commit()
    db.refresh(emp_rec)
    # print("json",emp_rec)
    return emp_rec

@app.get("/pd_filter/{pd_id}/",response_model=Product_Show)
def Product_single_rec(pd_id:int,db:Session=Depends(get_db)):
    std_rec=db.query(Product).filter(Product.pd_id==pd_id).first()
    if std_rec is None:
        raise HTTPException(status_code=404,detail="Product not found")
    return std_rec

@app.put("/pd_update/{pd_id}/",response_model=Product_Show)
def Product_update(pd_id:int,pd_upd:Product_Create,db:Session=Depends(get_db)):
    std_rec=db.query(Product).filter(Product.pd_id==pd_id).first()
    if std_rec is None:
        raise HTTPException(status_code=404,detail="student not found")
    std_rec.pd_id==pd_id
    std_rec.pd_name_name=pd_upd.pd_name
    std_rec.pd_price=pd_upd.pd_price
    db.commit()
    db.refresh(std_rec)
    return std_rec

@app.delete("/pd_delete/{pd_id}/")
def Product_delete(pd_id:int,db:Session=Depends(get_db)):
    emp_rec=db.query(Product).filter(Product.pd_id==pd_id).first()
    if emp_rec is None:
        raise HTTPException(status_code=404,detail="employee not found")
    db.delete(emp_rec)
    db.commit()
    # db.refresh(emp_rec)
    return {'msg':'category deleted succesfully'}