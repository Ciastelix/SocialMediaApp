from typing import List
from manageDB import createNewUser, authUser, getCurrentUser, oauth2Scheme, getAllUsers, getUserId, getUserName, createNewPost, getAllPosts, checkIfUserExists
from schemas import UserInPydantic, UserPydantic, UserPydanticToken, PostInPydantic, PostPydantic, UserLogPydantic
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


@app.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authUser(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    user_obj = await UserPydantic.from_tortoise_orm(user)
    token = jwt.encode(user_obj.dict(), "tykurwo")

    return {'access_token': token, 'token_type': 'bearer'}


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
        raise HTTPException(
            status_code=406, detail="User with this email/username already exists")


@app.get("/users", response_model=List[UserPydanticToken])
async def getUsers(token: UserPydantic = Depends(getCurrentUser)):
    return await getAllUsers()


@app.get("/user/{id}", response_model=UserPydantic)
async def getUserById(id: int, token: UserPydantic = Depends(getCurrentUser)):
    return await getUserId(id)


@app.post("/user/search/{name}", response_model=List[UserPydantic])
async def getUserByName(name: str, token: UserPydantic = Depends(getCurrentUser)):
    return await getUserName(name)


@app.get("/users/me", response_model=UserPydantic)
async def getUser(user: UserPydantic = Depends(getCurrentUser)):
    return user


@app.put("/user", response_model=UserPydantic)
async def alterUser(user: UserPydantic, token: UserPydantic = Depends(getCurrentUser)):
    return


@app.put("/posts", response_model=PostPydantic)
async def alterPost(post: PostInPydantic, token: UserPydantic = Depends(getCurrentUser)):
    return


@app.delete("/posts")
async def alterPost(post: PostInPydantic, token: UserPydantic = Depends(getCurrentUser)):
    return


@app.get("/posts", response_model=List[PostPydantic])
async def getPosts(token: UserPydantic = Depends(getCurrentUser)):
    return await getAllPosts()


@app.post("/posts/")
async def createPost(post: PostInPydantic):
    postObj = await createNewPost(post)
    await postObj.save()
    return await PostPydantic.from_tortoise_orm(postObj)
