from django.shortcuts import render
from .models import StarSystem

# Create your views here.
def space_view(request):
    star_systems = StarSystem.objects.all()
    context = {
                'title':"Space Map", 
                'SpaceSystems':star_systems
    }
    return render(request, "spacemap/space.html", context)