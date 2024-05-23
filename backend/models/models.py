from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from db import Database

Base = Database().Base

class ProductModel(Base):
    __tablename__ = "products"  # esse será o nome da tabela
    __table_args__ = {'schema': 'loja'}

    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String)
    preco = Column(Float)
    vendedor = Column(String)
    descricao = Column(String)
    quantidade = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=func.now())