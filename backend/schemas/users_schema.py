from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr
    is_active: bool

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        from_attributes = True

class UserUpdate(UserBase):
    password: Optional[str]
