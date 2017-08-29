from django.conf.urls import url, include
from .views import (register_in_site_post, register_info_view, login_view, character_view, login_in_site)

urlpatterns = [
    url(r'^register/$', register_info_view, name='register_info'),
    url(r'^register/post$', register_in_site_post, name='post_registration'),
    url(r'^login/$', login_view, name='login'),
    url(r'^login/post$', login_in_site, name='login'),
    url(r'^characters/$', character_view, name='characters'),
]