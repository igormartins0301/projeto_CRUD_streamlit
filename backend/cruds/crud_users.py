from sqlalchemy.orm import Session
from schemas.users_schema import UserBase, UserCreate, UserRead, UserUpdate
from models.users_models import UsersModel
from db import Database
from security import get_password_hash, verify_password
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

def get_user(db: Session, name: str):
    """
    Função que recebe um nome e senha e retorna a linha correspondente
    """
    return db.query(UsersModel).filter(UsersModel.name == name).first()

def authenticate_login(db: Session, email: str, password: str):
    db_user = db.query(UsersModel).filter(UsersModel.email == email).first()
    if not db_user or not verify_password(password, db_user.password):
        return None
    return db_user

def create_user(db: Session, user: UserCreate):
    try:
        hashed_password = get_password_hash(user.password)
        db_user = UsersModel(name=user.name, email=user.email, password=hashed_password, is_active=user.is_active)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback()
        if "ix_loja_users_email" in str(e):
            raise HTTPException(status_code=400, detail="Email already registered")
