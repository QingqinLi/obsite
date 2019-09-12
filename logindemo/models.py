from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    pws = models.CharField(max_length=32)

    class Meta:
        ordering = ("id",)
        db_table = "user"

