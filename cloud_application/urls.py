from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_airpollution$', airpollution, name='display_airpollution'),
    url(r'^display_waterpollution$', waterpollution, name='display_waterpollution'),
    url(r'^display_toxicgases$', airpollution, name='display_toxicgases'),
]