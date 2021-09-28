
from django.db import models
from django.db.models.fields import BooleanField, CharField, IntegerField, URLField
from django.db.models.fields.json import JSONField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class SocialMedia(models.Model):
    '''
    Model for which social media bot is going to be used 
    '''
    name = CharField(unique=True, null= False, blank= False,max_length=200)
    base_link= URLField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


class SocialMediaAuthUser(models.Model):
    '''
    Model for the account's that the bots will be using
    to log in their respective social medias.
    '''
    username = CharField(null= False, blank= False,max_length=200)
    password = CharField(max_length=200)
    is_active = BooleanField(default=True)
    social_media = ForeignKey(SocialMedia, null= False,blank=False,on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SocialMediaUser(models.Model):
    '''
    Model for the account that was scrapped
    '''
    class Meta:
        unique_together = ('username', 'social_media_id')
    username= CharField(max_length=200, null=False,blank=False)
    link = URLField(null=False,blank=False)
    social_media_id= ForeignKey(SocialMedia, int, null= False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    '''
    Model for the scrapped post from the SocialMediaUser
    account
    '''
    link = URLField(null=False,blank=False)
    metadata= JSONField(null= True)
    status= CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)