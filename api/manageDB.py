from models import User
from passlib.hash import bcrypt
from fastapi import Depends, status, HTTPException
from schemas import UserPydantic
from main import oauth2Scheme
import jwt
from os import environ


async def createUser(user):
    return User(username=user.username, passwordHash=bcrypt.hash(user.passwordHash))


async def authUser(username: str, password: str):
    user = await User.get(username=username)
    if not user:
        return False
    if not user.verifyPassword(password):
        return False
    return user


async def getCurrentUser(token: str = Depends(oauth2Scheme)):
    try:
        payload = jwt.decode(token, str(
            environ.get("JWT_SECRET")), algorithms=['HS256'])
        user = await User.get(id=payload.get('id'))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    return await UserPydantic.from_tortoise_orm(user)
