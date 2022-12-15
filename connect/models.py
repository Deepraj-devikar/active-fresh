from django.db import models
from django.contrib.auth.models import User 
from shop.models import Shop

class Phone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)    
    phone = models.CharField(max_length = 50)    

    def __str__(self):
        return self.phone

class Email(models.Model):
    user = models.ForeignKey(User, related_name="email_user", on_delete=models.CASCADE, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)    
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.email 

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)    
    detail = models.TextField()
    country = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    postalCode = models.PositiveIntegerField()
    latitude = models.DecimalField(max_digits=50, decimal_places=50)
    longitude = models.DecimalField(max_digits=50, decimal_places=50)

    def __str__(self):
        return self.detail 

class Info(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length = 150)
    message = models.TextField()
    
    
    
    
    