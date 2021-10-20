from tortoise import fields
from tortoise.models import Model
from passlib.hash import bcrypt


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    passwordHash = fields.CharField(120)

    def verifyPassword(self, password):
        return bcrypt.verify(password, self.passwordHash)
