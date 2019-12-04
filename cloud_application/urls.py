from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_airpollution$', airpollution, name='display_airpollution'),
]