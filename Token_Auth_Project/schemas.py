from pydantic import BaseModel

class RegisterUser(BaseModel):
    username:str
    password:str

class CreateResponse(BaseModel):
    id:int
    username:str
    # password:str
    class Config:
        orm_mode=True

class LoginUser(BaseModel):
    username:str
    password:str