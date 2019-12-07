from django import forms
from .models import *

'''class AirpollutionForm(forms.ModelForm):
    #state = forms.CharField()
    #pollutant = forms.CharField()
    #From = forms.ChoiceField(choices=[(x, x) for x in range(2010, 2020)])
    #To = forms.ChoiceField(choices=[(x, x) for x in range(2010, 2020)])
    pollutants_list_air=['CO','CO2','GHG','NOx','SOx','VOC']
    pollutant = forms.ChoiceField(choices=[(x,x) for x in pollutants_list_air])
    
    class Meta:
        model = AirPollution
        exclude = ('country','state','city','place','pollutants',)'''
        
class AirpollutionForm(forms.ModelForm):
    #state = forms.CharField()
    #pollutant = forms.CharField()
    #From = forms.ChoiceField(choices=[(x, x) for x in range(2010, 2020)])
    #To = forms.ChoiceField(choices=[(x, x) for x in range(2010, 2020)])
    pollutants_list_air=['CO','CO2','GHG','NOx','SOx','VOC']
    pollutant = forms.ChoiceField(choices=[(x,x) for x in pollutants_list_air])
    
    class Meta:
        model = airCO
        exclude = ('country','pollutants',)

class greenhouseForm(forms.ModelForm):
    #state = forms.CharField()
    #pollutant = forms.CharField()
    #From = forms.ChoiceField(choices=[(x, x) for x in range(2010, 2020)])
    #To = forms.ChoiceField(choices=[(x, x) for x in range(2010, 2020)])
    pollutants_list_water=['N','NH3','NO3','O2','P','PO4']
    pollutant = forms.ChoiceField(choices=[(x,x) for x in pollutants_list_water])
    
    class Meta:
        model = waterN
        exclude = ('country','pollutants',)
        
class deforestationForm(forms.ModelForm):
    country_list=['India','uganda','africa']
    degradation = forms.ChoiceField(choices=[(x,x) for x in country_list])
    class Meta:
        model = deforestation
        exclude = ('country','recent_year','value')