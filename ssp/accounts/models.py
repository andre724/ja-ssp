from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import EmailField

class SSPUser(AbstractUser):
    email= EmailField(null=False, blank= False)
