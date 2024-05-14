from sqlalchemy.orm import Session
from schemas.schemas import ProductUpdate, ProductCreate, ProductRead
from models.models import ProductModel
from db import Database

def get_product(db: Session, product_id: int):
    """
    Função que recebe um id e retorna a linha dele
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

def get_products(db: Session):
    """
    Função que retorna todos os elementos
    """
    return db.query(ProductModel).all()


def create_product(db: Session, product: ProductCreate):
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.produto is not None:
        db_product.produto = product.produto
    if product.descricao is not None:
        db_product.descricao = product.descricao
    if product.preco is not None:
        db_product.preco = product.preco
    if product.vendedor is not None:
        db_product.vendedor = product.vendedor
    if product.quantidade is not None:
        db_product.quantidade = product.quantidade

    db.commit()
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product