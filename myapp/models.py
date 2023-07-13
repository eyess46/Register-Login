from django.db import models
from datetime import datetime
import random
import string
from django.contrib.auth.models import User





class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=2)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2, default=2)

    def __str__(self):
        return f"{self.user.username}'s coinslord account"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=500, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=500, null=True)
    btc_address = models.CharField(max_length=500, null=True)
    etherum_address = models.CharField(max_length=500, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True)
 

    def __str__(self):
        return self.username

    




class Blog(models.Model):
    head = models.CharField(max_length=255)
    body = models.CharField(max_length=5000000)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=1000)


class ContactForm(models.Model):
    name = models.CharField(max_length= 100)
    subject = models.CharField(max_length= 100)
    email = models.EmailField(unique= True)
    message = models.CharField(max_length= 900)
    image = models.ImageField(upload_to= "images/")
