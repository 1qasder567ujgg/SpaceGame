from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def register_in_site_post(request):
    u_name = request.POST.get('user_name')
    u_email = request.POST.get('email')
    u_pass = request.POST.get('password')
    print(u_name, u_email, u_pass)
    User.objects.create_user(u_name, u_email, u_pass)
    # user.save()

    return HttpResponseRedirect('/login/')


def register_info_view(request):
    return render(request, 'character/registration.html', {'title':'Registration'})


def login_view(request):
    return render(request, 'character/login.html', {'title':'Login'})


@csrf_protect
def login_in_site(request):
    u_name = request.POST.get('user_name')
    u_pass = request.POST.get('password')
    user = authenticate(request, username=u_name, password=u_pass)
    print(user, u_name, u_pass)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/characters/')
    else:
        return HttpResponse('false')


def character_view(request):
    # print(request.user, request.user.is_authenticated)
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    return render(request, 'character/character.html', {'title':'Character'})

