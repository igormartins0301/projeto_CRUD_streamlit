from datetime import datetime, timedelta, timezone
from typing import Any, Union
from jose import jwt, JWTError
from passlib.context import CryptContext
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db import Database
from models.users_models import UsersModel
import os
import logging

logger = logging.getLogger(__name__)

db = Database()


load_dotenv()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None):
    if expires_delta:
        expire = datetime.now(tz=timezone.utc) + expires_delta
    else:
        expire = datetime.now(tz=timezone.utc) + timedelta(minutes=15)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/access-token/")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(db.get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        logger.info("Token JWT recebido: %s", token)
        
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        logger.info("Payload decodificado: %s", payload)
        
        user_id: str = payload.get("sub")  # Extraindo o ID do usuário do payload
        if user_id is None:
            logger.error("ID do usuário não encontrado no payload")
            raise credentials_exception
    except JWTError as e:
        logger.error("Erro ao decodificar o token JWT: %s", e)
        raise credentials_exception
    
    user = db.query(UsersModel).filter(UsersModel.id == int(user_id)).first()  # Buscando o usuário pelo ID
    
    if user is None:
        logger.error("Usuário não encontrado no banco de dados")
        raise credentials_exception
    
    logger.info("Usuário autenticado: %s", user.email)
    
    return user



