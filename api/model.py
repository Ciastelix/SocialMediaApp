from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String
import database


class Post(database.Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    createdBy = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", backref="creator")


class Friend(database.Base):
    __tablename__ = "friends"
    id = Column(Integer, primary_key=True, index=True)
    _id1 = Column(Integer)
    _id2 = Column(Integer)


class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, index=True)
    lastName = Column(String, index=True)
