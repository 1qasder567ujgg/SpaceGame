from django.conf.urls import url, include
from .views import (space_view, system_view, planet_view)

urlpatterns = [
    url(r'^space/$', space_view, name="space_map"),
    url(r'^space/(?P<s_id>[\w-]+)$', system_view, name="system_map"),
    url(r'^space/(?P<s_id>[\w-]+)/(?P<p_id>[\w-]+)$', planet_view, name="system_map"),
]
