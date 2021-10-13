from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import EmailField

class SSP_User(AbstractUser):
    email= EmailField(null=False, blank= False)
