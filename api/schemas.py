from tortoise.contrib.pydantic import pydantic_model_creator
from models import User, Post
UserPydantic = pydantic_model_creator(User, name="User")
UserInPydantic = pydantic_model_creator(
    User, name="UserIn", exclude_readonly=True)
UserLogPydantic = pydantic_model_creator(
    User, name="UserIn", exclude_readonly=True, exclude=("email", "phoneNumber"))
PostPydantic = pydantic_model_creator(Post, name="Post")
PostInPydantic = pydantic_model_creator(
    Post, name="PostIn", exclude_readonly=True)
UserPydanticToken = pydantic_model_creator(
    User, name="UserToken", exclude=("passwordHash"))
