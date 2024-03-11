from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to='user/profile_pics/', default='/user/profile_pics/default.png')


class SocialMediaField(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField()
    icon = models.ImageField(upload_to='user/profile_pics')


class SocialMediaRelationship(models.Model):
    social_media = models.ForeignKey(SocialMediaField, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    url = models.URLField()

