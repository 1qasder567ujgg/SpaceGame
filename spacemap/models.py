from django.db import models

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("space:system_map", kwargs={"id": self.id}) 


class Planet(models.Model):
    star_system = models.ForeignKey(StarSystem)
    inhabited = models.BooleanField(default=False)
    atmosphere = models.BooleanField(default=False)
    distance = models.FloatField()   
    diameter = models.FloatField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class City(models.Model):
    CITY_STAUS = (
        ('Village','Village'), 
        ('Town','Town'), 
        ('City','City')
        )
    planet = models.ForeignKey(Planet)
    inhabited = models.BooleanField(default=False)
    shop = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    space_port = models.BooleanField(default=False)
    population = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    city_status = models.CharField(max_length=10, choices=CITY_STAUS, default='Village')

    def __str__(self):
        return self.name

#TODO: Создать рандомные планеты для существующих звезд и города для планет