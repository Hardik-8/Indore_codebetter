from fastapi import FastAPI,HTTPException
from typing import List 
from pydantic import BaseModel

class Product(BaseModel):
    pd_id:int
    pd_name:str
    pd_price:int
    pd_category:str

app=FastAPI()

product_db:List[Product]=[]
@app.get("/product_list",response_model=list[Product])
def product_list_api():
    return product_db

@app.post("/pd_create",response_model=Product)
def product_create_list(pd_data:Product):
        for i in product_db:
            if i.pd_id==pd_data.pd_id:
                raise HTTPException(status_code=400,detail=("id number already exist"))
            
        product_db.append(pd_data)
        return pd_data

@app.get("/product/{pd_id}",response_model=Product)
def product_getid(pd_id:int):
    for i in product_db:
        if i.pd_id==pd_id:
            return i
            # break
        # else : 
    raise HTTPException(status_code=404,detail=("roll no not exist"))

@app.delete("/student_delete/{roll_no}", response_model=Product)
def student_delete_record(pd_id:int,pd_data:Product):
    for st in product_db:
        if st.pd_id==pd_data.pd_id:
            product_db.remove(pd_data)
            return pd_data
    raise HTTPException(status_code=404, detail=("Record not found"))