from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from security import get_current_user
from db import Database
from schemas.schemas import ProductRead, ProductUpdate, ProductCreate
from models.users_models import UsersModel
from typing import List
from cruds.crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product,
)

db = Database()
router = APIRouter()


@router.post("/products/", response_model=ProductRead)
def create_product_route(product: ProductCreate, db: Session = Depends(db.get_db), user: UsersModel = Depends(get_current_user)):
    return create_product(db=db, product=product)


@router.get("/products/", response_model=List[ProductRead])
def read_all_products_route(db: Session = Depends(db.get_db)):
    products = get_products(db)
    return products


@router.get("/products/{product_id}", response_model=ProductRead)
def read_product_route(product_id: int, db: Session = Depends(db.get_db)):
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.delete("/products/{product_id}", response_model=ProductRead)
def detele_product_route(product_id: int, db: Session = Depends(db.get_db), user: UsersModel = Depends(get_current_user)):
    db_product = delete_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/products/{product_id}", response_model=ProductRead)
def update_product_route(
    product_id: int, product: ProductUpdate, db: Session = Depends(db.get_db), user: UsersModel = Depends(get_current_user)
):
    db_product = update_product(db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/protected")
def protected_route(user: UsersModel = Depends(get_current_user)):
    return {"message": f"Hello, {user.name}!"}