
from typing import List, Optional

from pydantic import BaseModel


class RoleBase(BaseModel):
	name: str
	permissions: str


class RoleCreate(RoleBase):
	pass


class Role(RoleBase):
	id: int

	class Config:
		orm_mode = True


class UserCreate(BaseModel):
	username: str
	email: str
	password: str


class UserOut(BaseModel):
	id: int
	username: str
	email: str
	roles: List[Role]

	class Config:
		orm_mode = True

class Token (BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: Optional[str] = None
    permissions: Optional[List[str]] = None
    
class StudentBase (BaseModel):
    first_name: str 
    last_name: str
    email: str
    student_id: str
    grade: Optional[str] = None

class StudentCreate(StudentBase):
    pass
             
class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    grade: Optional[str] = None

class Student (StudentBase):
    id: int

    class Config:
        orm_mode = True     