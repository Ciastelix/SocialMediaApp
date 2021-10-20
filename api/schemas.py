from tortoise.contrib.pydantic import pydantic_model_creator
from models import User
UserPydantic = pydantic_model_creator(User, name="User")
UseerInPydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
UserPydanticToken = pydantic_model_creator(User, name="UserToken", exclude=("passwordHash")) 

