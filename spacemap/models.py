from django.db import models

# Create your models here.
class StarSystem(models.Model):
    """docstring for ClassName"""
    
    STAR_SIZE_PX = 5

    pos_x = models.IntegerField()
    pos_y = models.IntegerField(default=0)
    size = models.FloatField()
    color = models.CharField(max_length=8)
    temp = models.FloatField()
    name = models.CharField(max_length=50)
    mass = models.FloatField()
    #planets
    #stars

    def __str__(self):
        return self.name