from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from db import (
    getAllPosts,
    getPostByUserId,
    getProfilPage,
    searchUserProfile,
    userCreation,
    postCreation
)
from model import Post, User
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


@app.get("/")
async def root():
    return {"Hey": "Hello"}


@app.post("/api/create-user", tags=["Creation"])
async def createUser(userData: User) -> dict:
    res = await userCreation(userData.dict())
    return {"data": "Added"}


@app.get("/api/search-user/{name}", tags=["User"])
async def searchUserByName(name: str) -> dict:
    res = await searchUserProfile(name.split())

    return {"data": list(res)}


@app.get("/api/profil-page/{_id}", tags=["User"])
async def profilPage(_id: int) -> dict:
    res = await getProfilPage(_id)
    return {"data": list(res)}


@app.get("/api/show-post", tags=["Posts"])
async def showPosts() -> dict:
    res = await getAllPosts()
    return {"data": list(res)}


@app.get("/api/show-post/{_id}", tags=["Posts"])
async def showPostsOfUser(_id) -> dict:
    res = await getPostByUserId(_id)
    return {"data": list(res)}


@app.post("/api/add-post", tags=["Creation"])
async def addPost(postData: Post) -> dict:
    res = await postCreation(postData.dict())
    return {"data": "Added"}
