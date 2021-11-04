from tortoise import fields
from tortoise.models import Model
from passlib.hash import bcrypt


class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(32)
    content = fields.CharField(125)
    creator = fields.ForeignKeyField(
        'models.User', related_name='posts')


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    passwordHash = fields.CharField(120)
    phoneNumber = fields.CharField(12)
    email = fields.CharField(50, unique=True)

    def verifyPassword(self, password):
        return bcrypt.verify(password, self.passwordHash)
