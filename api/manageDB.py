from os import environ
import jwt
from fastapi import Depends, HTTPException, status
from passlib.hash import bcrypt
from fastapi.security import OAuth2PasswordBearer
from models import User, Post
from schemas import UserPydantic, UserPydanticToken, UserInPydantic, PostPydantic, PostInPydantic

oauth2Scheme = OAuth2PasswordBearer(tokenUrl="token")


async def createNewUser(user):
    return User(username=user.username, passwordHash=bcrypt.hash(user.passwordHash), phoneNumber=user.phoneNumber, email=user.email)


async def createNewPost(post, userId):
    return Post(title=post.title, content=post.content, creator_id=userId)


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

    return await UserPydanticToken.from_tortoise_orm(user)


async def getAllUsers():
    return await UserPydanticToken.from_queryset(User.all())


async def getAllPosts():
    return await PostPydantic.from_queryset(Post.all())


async def getUserId(id):
    return await User.get(id=id)


async def getUserName(name):
    return await UserPydantic.from_queryset(User.filter(username=name).all())


async def checkIfUserExists(email, name):
    if not await UserPydantic.from_queryset(User.filter(username=name).all()):
        if not await UserPydantic.from_queryset(User.filter(email=email).all()):
            return False
    else:
        return True
