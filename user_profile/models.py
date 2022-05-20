from ast import mod
from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import CustomeUserManager


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True, error_messages={"unique":"The email must be unique!"})
    profile_image = models.ImageField(null=True, blank = True, upload_to = "profile_images")
    REQUIRES_FIELDS = ["email"]
    objects = CustomeUserManager()
    followers = models.ManyToManyField("Follow")

    def __str__(self):
        return str(self.pk) + "." + self.username

    def get_profile_picture(self):
        url = ""
        try:
            url = self.profile_image.url

        except:
            url = ""
        return url

class Follow(models.Model):
    followed = models.ForeignKey(User, related_name='users_followers', on_delete=models.CASCADE)
    followed_by = models.ForeignKey(User, related_name='user_follows', on_delete=models.CASCADE)
    muted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return   str(self.pk) + "." + f"{self.followed_by.username} started following { self.followed.username }"