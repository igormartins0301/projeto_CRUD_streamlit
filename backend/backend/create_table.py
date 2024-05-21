from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db import Database
from datetime import datetime


db = Database()

Base = declarative_base()

class ProductTable(Base):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'loja'}

    id = Column(Integer, primary_key=True)
    produto = Column(String)
    preco = Column(Float)
    vendedor = Column(String)
    descricao = Column(String)
    quantidade = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

class UsersModel(Base):
    __tablename__ = "users"  # esse será o nome da tabela
    __table_args__ = {'schema': 'loja'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
Base.metadata.create_all(db.engine)


