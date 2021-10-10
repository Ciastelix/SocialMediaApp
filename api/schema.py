from pydantic import BaseModel


class EntryPost(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True


class GetPost(BaseModel):
    id: int
    title: str
    content: str
    createdBy: int

    class Config:
        orm_mode = True


class EntryFriend(BaseModel):
    id1: int
    id2: int

    class Config:
        orm_mode = True


class GetUser(BaseModel):
    id: int
    firstName: str
    lastName: str

    class Config:
        orm_mode = True


class EntryUser(BaseModel):
    firstName: str
    lastName: str

    class Config:
        orm_mode = True


class Name(BaseModel):
    name: str
