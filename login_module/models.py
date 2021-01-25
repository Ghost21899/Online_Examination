from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfiles(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    city=models.CharField(max_length=20, default="Anonymous")
    country=models.CharField(max_length=20, default="Anonymous")
    phone=models.BigIntegerField(default=0)
    img = models.ImageField(upload_to="user_images/")

    def __str__(self):
        return self.user