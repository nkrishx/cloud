from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_airpollution$', airpollution, name='display_airpollution'),
    url(r'^display_greenhouse$', greenhouse, name='display_greenhouse'),
    url(r'^display_deforestation$', deforestation, name='display_deforestation'),
    url(r'^display_about_us$', aboutus, name='display_about_us'),
   # url(r'^Services$', services, name='Services'),
]