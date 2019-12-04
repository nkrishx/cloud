# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AirPollution(models.Model):
    #Type = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    pollutants = models.CharField(max_length=200)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.pollutants

class WaterPollution(models.Model):
    #Type = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    pollutants = models.CharField(max_length=200)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.pollutants
