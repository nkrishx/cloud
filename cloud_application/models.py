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

class greenhouse(models.Model):
    #Type = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    pollutants = models.CharField(max_length=200)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.pollutants


class pollution(models.Model):
    country = models.CharField(max_length=30)
    pollutants = models.FloatField()
    
    class Meta:
        abstract = True
        
    def __str__(self):
        """Return a string representation of the model."""
        return self.country


class deforestation(models.Model):
    country = models.CharField(max_length=30)
    recent_year = models.DateField()
    value = models.FloatField()
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.country

class airCO(pollution):
    pass

class airCO2(pollution):
    pass
    
class airGHG(pollution):
    pass

class airNOX(pollution):
    pass
    
class airSOX(pollution):
    pass
    
class airVOC(pollution):
    pass
    
class waterN(pollution):
    pass
   
class waterNH3(pollution):
    pass

class waterNO3(pollution):
    pass
    
class waterO2(pollution):
    pass
    
class waterP(pollution):
    pass
    
class waterPO4(pollution):
    pass