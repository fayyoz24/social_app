from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.core.validators import RegexValidator


User = get_user_model()
# Create your models here.
class Profile(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user     = models.IntegerField()
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    bio         = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location    = models.CharField(max_length=100, blank=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    
    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user