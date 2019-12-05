# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from .models import *
from .forms import *
import csv
from django.utils.text import slugify
from django.http import HttpResponse
# Create your views here.

def index(request):
    items=AirPollution.objects.all()

    context = {
    }
    return render(request,'base.html', context)

'''def airpollution(request):
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
    items=airCO.objects.all()
    header='Currently Viewing Airpollution'
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
    'form' : form
    }
    return render(request, 'index.html', context)
    
def waterpollution(request):
    items=waterN.objects.all()
    header='Currently Viewing WaterPollution'
    if request.method == "POST":
        form = waterpollutionForm(request.POST)
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
                form = waterpollutionForm()
    else:
        form = waterpollutionForm()
    context={
    'header' : header,
    'items' : items,
    'form' : form
    }
    return render(request, 'index.html', context)
    