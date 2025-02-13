from django import forms
from django.db import models
from .models import Location

class LocationForm(forms.ModelForm):
    
    address_1 = forms.CharField(required=True)
    zip_code = forms.CharField(required=True)
    
    class Meta:
        model = Location
        fields= { 'address_2', 'address_1' ,'city','state','zip_code'}
        