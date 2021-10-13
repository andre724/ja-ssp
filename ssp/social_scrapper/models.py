
from django.db import models
from django.db.models.fields import BooleanField, CharField, URLField
from django.db.models.fields.json import JSONField
from django.db.models.fields.related import ForeignKey

STATUS_CHOICES = [
    ("FOUND", "FOUND"),
    ("SENT", "SENT"),
    ("WORKING", "WORKING"),
    ("DONE", "DONE"),
    ("ERROR", "ERROR"),
    ("MISSING", "MISSING")
]

class TrackingModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class SocialMedia(TrackingModel):
    '''
    Model that specifies which social medias the bots can be used on

    '''
    name = CharField(unique=True, null= False, blank= False,max_length=200)
    base_link= URLField(null=False, blank=False)



class SocialMediaAuthUser(TrackingModel):
    '''
    Model for the account's that the bots will be using
    to log in their respective social medias.
    '''
    username = CharField(null= False, blank= False,max_length=200)
    password = CharField(max_length=200)
    is_active = BooleanField(default=True)
    social_media = ForeignKey(SocialMedia,on_delete= models.PROTECT)
   

class SocialMediaUser(TrackingModel):
    '''
    Model for the account that was scrapped
    '''
    class Meta:
        unique_together = ('username', 'social_media')
    username= CharField(max_length=200, null=False,blank=False)
    link = URLField(null=False,blank=False)
    social_media= ForeignKey(SocialMedia,on_delete=models.PROTECT )



class Post(TrackingModel):
    '''
    Model for the scrapped post from the SocialMediaUser
    account
    '''
    user= ForeignKey(SocialMediaUser, on_delete=models.PROTECT)
    link = URLField(null=False,blank=False)
    metadata= JSONField(null= True)
    status= CharField(max_length=10, choices= STATUS_CHOICES)
    post_type= CharField(max_length= 200, default= 'Image')
