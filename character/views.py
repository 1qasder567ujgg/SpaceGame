from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def register_view(reqest):
    u_name = reqest.GET.get('user_name')
    u_email = reqest.GET.get('email')
    u_pass = reqest.GET.get('password')

    User.object.create_user(u_name, u_email, u_pass)

    return HttpResponseRedirect('/login/')


def register_info_view(reqest):
    return render(reqest, 'character/reister.html', {'title':'Registration'})


def login_view(reqest):
    return render(reqest, 'character/login.html', {'title':'Login'})


def character_view(reqest):
    return render(reqest, 'character/character.html', {'title':'Character'})