from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db import Database

Base = Database().Base

class UsersModel(Base):
    __tablename__ = "users"  # esse será o nome da tabela
    __table_args__ = {'schema': 'loja'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
    is_active = Column(Boolean)
