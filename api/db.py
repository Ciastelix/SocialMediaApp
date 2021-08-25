from pymongo import MongoClient
import pymongo
from random import randint, choice
from string import ascii_letters


def get_database():
    client = MongoClient(
        "mongodb+srv://Mateusz:Q7e2fhwevHCKr6sg@cluster0.e9nku.mongodb.net/test"
    )
    return client['photos']


dbname = get_database()
collN = dbname['photos']
collN.create_index("_id")


async def fetchAllPhotos():
    res = collN.find()

    return res


async def fetchOnePhoto(id):
    return collN.find({"_id": id})


async def fetchPhotoByTag(tag):
    return collN.find({"tag": tag})


async def insertPhoto(photo):
    letters = [i for i in ascii_letters]
    while True:
        url = ""
        for _ in range(20):
            url += choice(letters)
        url += ".jpg"
        if not list(collN.find({"url": url})):
            photo['url'] = url
            break
    while True:
        aId = randint(0, 1000000)
        if not list(collN.find({"_id": aId})):
            photo['_id'] = aId
            break
    allTags = photo['tag'].strip().split(" #")
    allTags[0] = allTags[0][1:]
    photo['tag'] = list(set(allTags))
    inserted = collN.insert_one(photo)
    return url


async def alterPhoto(_id, body):
    collN.update_one({"_id": _id}, {"$set": body})
    return collN.find({"_id": _id})


async def removePhoto(_id):
    collN.delete_one({"_id": _id})
    return 1


async def getAllTags():
    tags = []
    for i in collN.find():
        tags += i['tag']
    return set(tags)
