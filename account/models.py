from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.db import models

<<<<<<< HEAD
'''class MyUserManager(BaseUserManager):
=======
class MyUserManager(BaseUserManager):
>>>>>>> 140d16638259d6faea57a2334bd2d992bd24bf3c
    def create_user(self, email, photo, password=None):

        user = self.model(
            email=self.normalize_email(email),
            photo=photo,
        )

        user.set_password(password)
        user.save(using=self._db)
<<<<<<< HEAD
        return user'''
=======
        return user
>>>>>>> 140d16638259d6faea57a2334bd2d992bd24bf3c

class User(AbstractUser):
    # add additional fields in here
    photo = models.ImageField(upload_to='user/%Y/%m/%d')
<<<<<<< HEAD
    #REQUIRED_FIELDS = [ "photo" ]
    #objects = MyUserManager()
=======
    REQUIRED_FIELDS = [ "photo" ]
    objects = MyUserManager()
>>>>>>> 140d16638259d6faea57a2334bd2d992bd24bf3c

    def __str__(self):
        return self.username
