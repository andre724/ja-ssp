
from django.db import models
from django.db.models.fields import BooleanField, CharField, IntegerField, URLField
from django.db.models.fields.json import JSONField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class SocialMedia(models.Model):
    name = CharField(unique=True, null= False, blank= False,max_length=200)
    base_link= URLField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


class SocialMediaAuthUser(models.Model):
    username = CharField(null= False, blank= False,max_length=200)
    password = CharField(max_length=200)
    is_active = BooleanField(default=True)
    social_media_id = ForeignKey(SocialMedia, int, null= False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SocialMediaUser(models.Model):
    class Meta:
        unique_together = ('username', 'social_media_id')
    username= CharField(max_length=200, null=False,blank=False)
    link = URLField(null=False,blank=False)
    social_media_id= ForeignKey(SocialMedia, int, null= False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    link = URLField(null=False,blank=False)
    metadata= JSONField()
    status= CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)