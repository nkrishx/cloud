# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
#from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(AirPollution)
admin.site.register(airCO)
admin.site.register(airCO2)
admin.site.register(airGHG)
admin.site.register(airNOX)
admin.site.register(airSOX)
admin.site.register(airVOC)
admin.site.register(waterN)
admin.site.register(waterNH3)
admin.site.register(waterNO3)
admin.site.register(waterO2)
admin.site.register(waterP)
admin.site.register(waterPO4)