from django.shortcuts import render
from .models import StarSystem, Planet, City

# Create your views here.
def space_view(request):
    star_systems = StarSystem.objects.all()
    context = {
                'title':"Space Map", 
                'SpaceSystems':star_systems
    }
    return render(request, "spacemap/space.html", context)


def system_view(request, s_id):
    star = StarSystem.objects.get(id=int(s_id))
    print(request.user)
    planets = Planet.objects.filter(star_system=star)
    context = {
                'title':'Start System Map', 
                'Star':star,
                'Planets':planets
    }
    return render(request, "spacemap/starsystem.html", context)


def planet_view(request, p_id, s_id):
    star = StarSystem.objects.get(id=int(s_id))
    planet = Planet.objects.get(id=int(p_id))
    cities = City.objects.filter(planet=planet)
    context = {
                'title':'Planet Map', 
                'Star':star,
                'Planet':planet,
                'Cities':cities
    }
    return render(request, "spacemap/planet.html", context)