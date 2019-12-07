# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from .models import *
from .forms import *
import csv
from django.utils.text import slugify
from django.http import HttpResponse
from IPython.display import IFrame
import commands
#from pyhive import hive
# Create your views here.

def index(request):
    items=AirPollution.objects.all()
    context = {
    }
    return render(request,'home.html', context)

'''def services(request):
    return render(request,'services.html')
def airpollution(request):
    items=AirPollution.objects.all()
    header='Currently Viewing Airpollution'
    startyear=''
    endyear=''
    if request.method == "POST":
        form = AirpollutionForm(request.POST)
        if form.is_valid():
            output = []
            state = form.cleaned_data['state']
            items=AirPollution.objects.filter(state=state)
            model_name = slugify(items.model.__name__)
           # BASE_DIR = "/home/ubuntu/server/cloud_application/"
           # path = os.path.join(os.path.dirname(BASE_DIR), 'csvstorage')
            path = r"/home/ubuntu/server/cloud_assignment/csvstorage"
            if not os.path.exists(path):
                os.mkdir(path)
            filename = str(state)+"{}.csv".format(model_name)
            filepath = os.path.join(path, filename)
           # header=['country', 'state', 'city', 'place','pollutants']
            with open(filepath, 'w') as my_file:
                #writer = csv.DictWriter(my_file,fieldnames=header)
                writer = csv.writer(my_file)
                writer.writerow(['country', 'state', 'city', 'place','pollutants'])
                for each in items:
                        output.append([each.country, each.state, each.city, each.place, each.pollutants])
                writer.writerows(output)
                form = AirpollutionForm()
    else:
        form = AirpollutionForm()
    context={
    'header' : header,
    'items' : items,
    'form' : form,
    'startyear' : startyear,
    'endyear' : endyear
    }
    return render(request, 'index.html', context)'''
    
def airpollution(request):
    #tab_obj=r"https://public.tableau.com/views/RecordsLost/Dashboard?:embed=y&:display_count=yes&:showVizHome=no"
    tab_obj_air=r"https://public.tableau.com/views/AirPollution_15756715183790/Dashboard1?:embed=y&:display_count=yes&:showVizHome=no"
    items=airCO.objects.all()
    header='Currently Viewing Airpollution'
    cmd = "hive -S -e 'SELECT * FROM default.airpollution;'"
    if request.method == "POST":
        form = AirpollutionForm(request.POST)
        if form.is_valid():
            output = []
            pollutant = form.cleaned_data['pollutant']
            pollutants_dict_air={
            'CO':airCO,
            'CO2':airCO2,
            'GHG':airGHG,
            'NOx':airNOX,
            'SOx':airSOX,
            'VOC':airVOC
            }
            for each in pollutants_dict_air:
                if each.lower() == pollutant.lower():
                    print type(airCO)
                    items=pollutants_dict_air[each].objects.all()
                    break
            model_name = slugify(items.model.__name__)
            path = "C:\\Users\\navee\\Desktop\\cloud\\data_set"
           # BASE_DIR = "/home/ubuntu/server/cloud_application/"
           # path = os.path.join(os.path.dirname(BASE_DIR), 'csvstorage')
           # path = r"/home/ubuntu/server/cloud_assignment/csvstorage"
            if not os.path.exists(path):
                os.mkdir(path)
            filename = str(pollutant)+"{}.csv".format(model_name)
            filepath = os.path.join(path, filename)
           # header=['country', 'state', 'city', 'place','pollutants']
            with open(filepath, 'w') as my_file:
                #writer = csv.DictWriter(my_file,fieldnames=header)
                writer = csv.writer(my_file)
                writer.writerow(['country','pollutants'])
                for each in items:
                        output.append([each.country, each.pollutants])
                writer.writerows(output)
                form = AirpollutionForm()
    else:
        form = AirpollutionForm()
    context={
    'header' : header,
    'items' : items,
    'form' : form,
    'tab_obj' : tab_obj_air
    }
    return render(request, 'airpollution.html', context)
    
def greenhouse(request):
    items=waterN.objects.all()
    tab_obj_greenhouse=r"https://public.tableau.com/views/GreenHouseGasesEmissionAnalysis_15756956448950/GHGDashboard-Overview?:embed=y&:display_count=yes&:showVizHome=no"
    header='Currently Viewing Green House Gas emission data'
    cmd = "hive -S -e 'SELECT * FROM default.greenhouse;'"
    if request.method == "POST":
        form = greenhouseForm(request.POST)
        if form.is_valid():
            output = []
            pollutant = form.cleaned_data['pollutant']
            pollutants_dict_water={
            'N':waterN,
            'NH3':waterNH3,
            'NO3':waterNO3,
            'O2':waterO2,
            'P':waterP,
            'PO4':waterPO4
            }
            for each in pollutants_dict_water:
                if each.lower() == pollutant.lower():
                    items=pollutants_dict_water[each].objects.all()
                    break
            model_name = slugify(items.model.__name__)
            path = "C:\\Users\\navee\\Desktop\\cloud\\data_set"
           # BASE_DIR = "/home/ubuntu/server/cloud_application/"
           # path = os.path.join(os.path.dirname(BASE_DIR), 'csvstorage')
           # path = r"/home/ubuntu/server/cloud_assignment/csvstorage"
            if not os.path.exists(path):
                os.mkdir(path)
            filename = str(pollutant)+"{}.csv".format(model_name)
            filepath = os.path.join(path, filename)
           # header=['country', 'state', 'city', 'place','pollutants']
            with open(filepath, 'w') as my_file:
                #writer = csv.DictWriter(my_file,fieldnames=header)
                writer = csv.writer(my_file)
                writer.writerow(['country','pollutants'])
                for each in items:
                        output.append([each.country, each.pollutants])
                writer.writerows(output)
                form = greenhouseForm()
    else:
        form = greenhouseForm()
    context={
    'header' : header,
    'items' : items,
    'form' : form,
    'tab_obj' : tab_obj_greenhouse
    }
    return render(request, 'greenhouse.html', context)
    
    
def deforestation(request):
    #items=deforestation.objects.all()
    tab_obj_deforestation=r"https://public.tableau.com/views/Deforestationfrom1990-2016_15756963168260/Deforestationfrom1990-2016?:embed=y&:display_count=yes&:showVizHome=no"
    header = "Currently viewing deforestation data"
    cmd = "hive -S -e 'SELECT * FROM default.deforestation;'"
    if request.method == "POST":
        form = deforestationForm(request.POST)
        if form.is_valid():
            output = []
            degradation = form.cleaned_data['degradation']
            if each.lower() == degradation.lower():
                items=deforestation.objects.all()
            model_name = slugify(items.model.__name__)
            path = "C:\\Users\\navee\\Desktop\\cloud\\data_set"
           # BASE_DIR = "/home/ubuntu/server/cloud_application/"
           # path = os.path.join(os.path.dirname(BASE_DIR), 'csvstorage')
           # path = r"/home/ubuntu/server/cloud_assignment/csvstorage"
            if not os.path.exists(path):
                os.mkdir(path)
            filename = str(pollutant)+"{}.csv".format(model_name)
            filepath = os.path.join(path, filename)
           # header=['country', 'state', 'city', 'place','pollutants']
            with open(filepath, 'w') as my_file:
                #writer = csv.DictWriter(my_file,fieldnames=header)
                writer = csv.writer(my_file)
                writer.writerow(['country','pollutants'])
                for each in items:
                        output.append([each.country, each.pollutants])
                writer.writerows(output)
                form = deforestationForm()
    else:
        form = deforestationForm()
    context={
    'header' : header,
    'tab_obj' : tab_obj_deforestation
    }
    return render(request, 'deforestation.html', context)
    
def aboutus(request):
    return render(request, 'about.html')