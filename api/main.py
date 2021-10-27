from typing import List
from manageDB import createNewUser, authUser, getCurrentUser, oauth2Scheme, getAllUsers, getUserId, getUserName, createNewPost, getAllPosts, checkIfUserExists
from schemas import UserInPydantic, UserPydantic, UserPydanticToken, PostInPydantic, PostPydantic
from models import User
import jwt
from os import environ
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import FastAPI, Depends, HTTPException, status
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ['models']},
    generate_schemas=True,
    add_exception_handlers=True
)


@app.post("/token")
async def generateToken(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authUser(form_data.username, form_data.password)
    if not user:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    userObj = await UserPydantic.from_tortoise_orm(user)

    token = jwt.encode(userObj.dict(), str(environ.get("JWT_SECRET")))
    return {"access_token": token, "token_type": "bearer"}


@app.post("/")
async def index(token: str = Depends(oauth2Scheme)):
    return {"access_token": token}


@app.post("/users")
async def createUser(user: UserInPydantic):
    if not await checkIfUserExists(user.email, user.username):
        userObj = await createNewUser(user)
        await userObj.save()
        return await UserPydantic.from_tortoise_orm(userObj)
    else:
        return HTTPException(status_code=406, detail="User with this email/username already exists")


@app.get("/users", response_model=List[UserPydanticToken])
async def getUsers(user: UserPydantic = Depends(getCurrentUser)):
    return await getAllUsers()


@app.get("/user/{id}", response_model=UserPydantic)
async def getUserById(id: int, user: UserPydantic = Depends(getCurrentUser)):
    return await getUserId(id)


@app.post("/user/search/{name}", response_model=List[UserPydantic])
async def getUserByName(name: str, user: UserPydantic = Depends(getCurrentUser)):
    return await getUserName(name)


@app.get("/users/me", response_model=UserPydantic)
async def getUser(user: UserPydantic = Depends(getCurrentUser)):
    return user


@app.get("/posts/", response_model=List[PostPydantic])
async def getPosts(user: UserPydantic = Depends(getCurrentUser)):
    return await getAllPosts()


@app.post("/posts/", response_model=PostPydantic)
async def createPost(post: PostInPydantic, user: UserPydantic = Depends(getCurrentUser)):
    postObj = await createNewPost(post, user.id)
    await postObj.save()
    return await PostPydantic.from_tortoise_orm(postObj)
