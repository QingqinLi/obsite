from django.db import models


# Create your models here.
class Hobby(models.Model):
    name = models.CharField(max_length=32)

