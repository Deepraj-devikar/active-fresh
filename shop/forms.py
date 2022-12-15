from django.core import validators
from django import forms 
from .models import Shop

class ShopActivation(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'openingTime', 'closingTime']
        