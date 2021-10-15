from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserAccount(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    email = models.EmailField(max_length=100, blank=False, null=False)
