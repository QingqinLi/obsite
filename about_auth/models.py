from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    phone = models.CharField(max_length=11)