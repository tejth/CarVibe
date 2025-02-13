from django import forms
from django.db import models
from .models import Location , Profile
from localflavor.us.forms import USZipCodeField
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name')


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model =Profile
        fields = ('photo','bio','phone_number')


class LocationForm(forms.ModelForm):
    
    address_1 = forms.CharField(required=True)
    zip_code = forms.CharField(required=True)
    
    class Meta:
        model = Location
        fields= { 'address_2', 'address_1' ,'city','state','zip_code'}
        