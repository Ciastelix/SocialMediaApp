from pymongo import MongoClient
import pymongo
from random import randint


def get_database():
    client = MongoClient(
        "mongodb+srv://Mateusz:Q7e2fhwevHCKr6sg@cluster0.e9nku.mongodb.net/test"
    )
    return client['socialApp']


dbname = get_database()


def defineCollectionName(mode):
    if mode == "user":
        collN = dbname['users']
    elif mode == "post":
        collN = dbname['posts']
    else:
        return 0
    collN.create_index("_id")
    return collN


async def getAllPosts():
    collN = defineCollectionName("post")
    return collN.find()


async def getPostByUserId(_id):
    collN = defineCollectionName("post")
    return collN.find({"createdBy": int(_id)})


async def getProfilPage(_id):
    collN = defineCollectionName("user")
    return collN.find_one({"_id": _id})


async def searchUserProfile(name):
    collN = defineCollectionName("user")
    if len(name) == 1:
        return collN.find({"firstName": name[0]})
    elif len(name) == 2:
        return collN.find({"$and": [{"firstName": name[0]}, {"lastName": name[1]}]})


async def userCreation(userData):
    collN = defineCollectionName("user")
    while True:
        _id = randint(0, 1000000)
        if not list(collN.find({"_id": _id})):
            userData['_id'] = _id
            break
    inserted = collN.insert_one(userData)
    return inserted


async def postCreation(postData):
    collN = defineCollectionName("post")
    while True:
        _id = randint(0, 1000000)
        if not list(collN.find({"_id": _id})):
            postData['_id'] = _id
            break
    inserted = collN.insert_one(postData)
    return 1

