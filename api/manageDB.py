import model
import schema
from sqlalchemy.orm import Session
from random import randint


def getAllPosts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Post).offset(skip).limit(limit).all()


def getPostByUserId(db: Session, usr: schema.EntryUser):
    return usr.posts


def getProfilPage(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()


def searchUserProfile(db: Session, name: str):
    name = name.name.split()
    if len(name) == 2:
        return db.query(model.User).filter(model.User.firstName == name[0] & model.User.lastName == name[1]).all()
    return db.query(model.User).filter(model.User.firstName == name[0]).all()


def userCreation(db: Session, user: schema.EntryUser):
    while True:
        id = randint(0, 100000000)
        if not db.query(model.User).filter(model.User.id == id).first():
            db_user = model.User(**user.dict(), id=id)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
        break
    return db_user


def postCreation(db: Session, post: schema.EntryPost, user_id: int):
    db_post = model.Post(**post.dict(), createdBy=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def getUser(db: Session, _id: int):
    return db.query(model.User).filter(model.User.id == _id).first()


def getAllUsers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()
