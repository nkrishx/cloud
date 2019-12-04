from django import forms
from .models import *

class AirpollutionForm(forms.ModelForm):
    state = forms.CharField()
    #From = forms.ChoiceField(choices=[(x, x) for x in range(2010, 2020)])
    #To = forms.ChoiceField(choices=[(x, x) for x in range(2010, 2020)])
    
    class Meta:
        model = AirPollution
        exclude = ('country','state','city','place','pollutants',)
