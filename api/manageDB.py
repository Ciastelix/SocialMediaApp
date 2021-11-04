from os import environ
import jwt
from fastapi import Depends, HTTPException, status
from passlib.hash import bcrypt
from fastapi.security import OAuth2PasswordBearer
from models import User, Post
from schemas import UserPydantic, UserPydanticToken, PostPydantic

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
        payload = jwt.decode(token, str(environ.get(
            "JWT_SECRET")), algorithms=['HS256'])
        user = await User.get(id=payload.get('id'))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    return await UserPydantic.from_tortoise_orm(user)


async def getAllUsers():
    return await UserPydanticToken.from_queryset(User.all())


async def getAllPosts():
    return await PostPydantic.from_queryset(Post.all())


async def getUserId(id):
    return await User.get(id=id)


async def getUserName(name):
    return await UserPydantic.from_queryset(User.filter(username=name).all())


async def checkIfUserExists(email, name):
    if not await UserPydantic.from_queryset(User.filter(username=name).exists()):
        if not await UserPydantic.from_queryset(User.filter(email=email).exists()):
            return False
    else:
        return True


async def updateUser(user, userId):
    usr = user.dict(exclude_unset=True)
    usr["passwordHash"] = bcrypt.hash(user.passwordHash)
    print(usr)
    await User.filter(id=userId).update(**usr)
    return await UserPydantic.from_queryset_single(User.get(id=userId))


async def updatePost(post):
    post = post.dict(exclude_unset=True)
    postId = post["id"]
    print(Post.get(id=postId))
    del post["id"]
    await Post.filter(id=postId).update(**post)
    return await PostPydantic.from_queryset_single(Post.get(id=postId))
