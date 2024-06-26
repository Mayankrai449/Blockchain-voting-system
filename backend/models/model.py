from pydantic import BaseModel, Field, EmailStr
from fastapi import Form

    
class UserRegSchema(BaseModel):
    username: str
    fullname: str
    email: EmailStr
    dob: str 
    age: int = Field(default=None)
    city: str = Field(default=None),
    password: str
    disabled: bool = Field(default=False)
    
    @classmethod
    def form(
        cls,
        username: str = Form(...),
        fullname: str = Form(...),
        email: EmailStr = Form(...),
        dob: str = Form(...),
        city: str = Form(...),
        password: str = Form(...)
    ):
        return cls(
            username=username,
            fullname=fullname,
            email=email,
            dob=dob,
            city=city,
            password=password
        )
    
 
class UserLoginSchema(BaseModel):
    username: str = Field(default=None),
    password: str = Field(default=None),
    
    @classmethod
    def form(
        cls,
        username: str = Form(...),
        password: str = Form(...)
    ):
        return cls(
            username=username,
            password=password
        )
        
        
class User(BaseModel):
    user: str
    email: EmailStr
    

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str = None
    
class UserPass(BaseModel):
    hashed_password: str