from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database
import manageDB
# (
#     getAllPosts,
#     getPostByUserId,
#     getProfilPage,
#     searchUserProfile,
#     userCreation,
#     postCreation,
#     addFriend,
#     showFriendReq,
#     # showAllFriends,
#     getUser
# )
import schema
import model
from typing import List
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
database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schema.EntryUser)
def create_user(user: schema.EntryUser, db: Session = Depends(get_db)):
    return manageDB.userCreation(db=db, user=user)


@app.get("/users/", response_model=List[schema.EntryUser])
def getAllUsers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = manageDB.getAllUsers(db, skip=skip, limit=limit)
    return users


@app.get("/user/{_id}", response_model=List[schema.GetUser])
def getUser(_id, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = manageDB.getPostByUserId(db, _id=_id, skip=skip, limit=limit)
    return users


@app.post("/add/post", response_model=schema.EntryPost)
def add_post(post: schema.EntryPost, db: Session = Depends(get_db)):
    return manageDB.postCreation(db=db, post=post, user_id=77448781)


@app.get("/get/posts", response_model=List[schema.GetPost])
def get_post(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return manageDB.getAllPosts(db, skip=skip, limit=limit)


@app.post("/search/user", response_model=List[schema.GetUser])
def searchUser(name: schema.Name, db: Session = Depends(get_db)):
    return manageDB.searchUserProfile(db, name=name)
