import datetime
from jose import jwt
from fastapi import HTTPException
from passlib.context import CryptContext
from pydantic import EmailStr
from app.config import settings

from app.registration.dao import UsersDao

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hash_password) -> bool:
    return pwd_context.verify(plain_password, hash_password)

async def authenticate_user(email: EmailStr, password: str):
    existing_user =  await UsersDao.find_one_or_none(email=email)
    if not existing_user and not verify_password(password, existing_user.password):
        return None
    
    return existing_user

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.datetime.now() + datetime.timedelta(days=365)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        settings.ALGORITHM)
    return encode_jwt