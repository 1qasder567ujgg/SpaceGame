from django.conf.urls import url, include
from .views import (register_view, register_info_view, login_view)

urlpatterns = [
    url(r'^register/$', register_info_view, name='register_info'),
    url(r'^register/post$', register_view, name='post_registration'),
    url(r'^login/$', login_view, name='login'),
]