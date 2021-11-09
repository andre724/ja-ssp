from django.db import models
from django.contrib.auth.models import AbstractUser


class SSPUser(AbstractUser):
    email= models.EmailField(null=False, blank= False)
