from django.db import models
from django.contrib.auth.models import User
from localflavor.in_.models import INStateField
import re
from django.core.exceptions import ValidationError

# Custom validator for Indian zip code
def validate_in_zip_code(value):
    if not re.match(r'^\d{6}$', value):
        raise ValidationError('Invalid ZIP Code. It should be 6 digits.')

class Location(models.Model):
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = INStateField(default='KA')
    zip_code = models.CharField(max_length=6, validators=[validate_in_zip_code], default='000000')  # Temporary default value
    
    def __str__(self):
        return f'Location {self.id}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
