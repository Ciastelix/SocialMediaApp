from pydantic import BaseModel


class Post(BaseModel):
    _id: int
    title: str
    content: str
    createdBy: int


class User(BaseModel):
    _id: int
    firstName: str
    lastName: str


class EntryPost(BaseModel):
    title: str
    content: str


class EntryUser(BaseModel):
    firstName: str
    lastName: str
