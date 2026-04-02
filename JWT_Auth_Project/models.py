from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

user_roles = Table(
    "user roles", 
     Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("role_id", Integer, ForeignKey("roles.id"))
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True, index=True, nullable=False)
    email = Column(String(20), unique=True, nullable=False)
    password = Column(String(254), nullable=False)
    roles = relationship("Role", secondary=user_roles, back_populates="users")
    
class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True, index=True, nullable=False)
    permissions = Column(String(20), nullable=False)
    users = relationship("User", secondary=user_roles, back_populates="roles")
    
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), unique=True, nullable=False)
    student_id = Column(String(20), unique=True, nullable=False )
    grade=  Column(String(20), nullable=False)
    