from django.shortcuts import render
from .models import StarSystem, Planet

# Create your views here.
def space_view(request):
    star_systems = StarSystem.objects.all()
    context = {
                'title':"Space Map", 
                'SpaceSystems':star_systems
    }
    return render(request, "spacemap/space.html", context)


def system_view(request, id):
    star = StarSystem.objects.get(id=int(id))

    planets = Planet.objects.filter(star_system=star)
    context = {
                'title':'Planet Map', 
                'Star':star,
                'Planets':planets
    }
    return render(request, "spacemap/starsystem.html", context)