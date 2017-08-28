from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Character(models.Model):
    user_id = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    points = models.IntegerField(default=0) 

    def __str__(self):
        return self.name