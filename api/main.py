from manageDB import createUser, authUser, getCurrentUser
from schemas import UseerInPydantic, UserPydantic
import jwt
from os import environ
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
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


oauth2Scheme = OAuth2PasswordBearer(tokenUrl="token")
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ['models']},
    generate_schemas=True,
    add_exception_handlers=True
)
# TODO: manage posts and users


@app.post("/token")
async def geenerateToken(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authUser(form_data.username, form_data.password)
    if not user:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    userObj = await UserPydantic.from_tortoise_orm(user)

    token = jwt.encode(userObj.dict(), str(environ.get("JWT_SECRET")))
    return {"access_token": token, "token_type": "bearer"}


@app.get("/")
async def index(token: str = Depends(oauth2Scheme)):
    return {"the_token": token}


@app.post("/users", response_model=UserPydantic)
async def createUser(user: UseerInPydantic):
    userObj = await createUser(user)
    await userObj.save()
    return await UserPydantic.from_tortoise_orm(userObj)


@app.get("/users/me", response_model=UserPydantic)
async def getUser(user: UserPydantic = Depends(getCurrentUser)):
    return user

@app.get("/posts/")
async def getPosts():
    posts = await getPosts