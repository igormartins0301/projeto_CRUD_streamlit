from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    produto: str
    preco: float
    vendedor: str
    descricao: str
    quantidade: int

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id:int
    created_at:datetime
    
    class Config:
        from_attributes = True

class ProductUpdate(ProductBase):
    produto: Optional[str] = None
    preco: Optional[float] = None
    vendedor: Optional[str] = None
    descricao: Optional[str] = None
    quantidade: Optional[int] = None


