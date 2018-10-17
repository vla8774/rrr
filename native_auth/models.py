
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    photo = models.ImageField(upload_to='user/%Y/%m/%d')

    REQUIRED_FIELDS = [ "photo" ]

