from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import Database
from datetime import timedelta
from schemas.users_schema import UserBase, UserCreate, UserRead, UserUpdate, Token
from typing import List
from cruds.crud_users import (
    get_user,
    create_user,
    authenticate_login
)
from security import create_access_token

db = Database()
router_user = APIRouter()

@router_user.post("/users/", response_model=UserRead)
def create_user_route(user: UserCreate, db: Session = Depends(db.get_db)):
    return create_user(db=db, user=user)

# @router_user.post("/login", response_model=UserRead)
# def login_user_route(email: str, password: str, db: Session = Depends(db.get_db)):
#     db_user = authenticate_login(db, email=email, password=password)
#     if db_user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect email/password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return db_user

@router_user.post("/login", response_model=Token)
def login_user_route(email: str, password: str, db: Session = Depends(db.get_db)):
    db_user = authenticate_login(db, email=email, password=password)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email/password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=15)
    access_token = create_access_token(
        subject=str(db_user.id), expires_delta=access_token_expires
    )
    
    return Token(access_token=access_token)

@router_user.get("/users/{name}", response_model=UserRead)
def read_user_route(name: str, password: str, db: Session = Depends(db.get_db)):
    db_user = get_user(db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

