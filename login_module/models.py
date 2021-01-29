from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    city=models.CharField(max_length=20, default="Anonymous")
    country=models.CharField(max_length=20, default="Anonymous")
    phone=models.BigIntegerField(default=0)
    img = models.ImageField(upload_to="user_images/")
    img_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.get_or_create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)