# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models import ForeignKey
from datetime import datetime

from django.forms import ModelForm, forms


class City(models.Model):
    name = models.CharField(max_length=50, null=False)


class Country(models.Model):
    name = models.CharField(max_length=50, null=False)

class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=500, null=True)

class TypeMultimedia(models.Model):
     name = models.CharField(max_length=50, null=False)
     description = models.CharField(max_length=500, null=True)


class UserGallery(models.Model):
    user_session = models.CharField(max_length=100,null=False)
    name = models.CharField(max_length=100,null=False)
    email = models.CharField(max_length=150,null=False)
    password = models.CharField(max_length=15,null=False)
    image = models.ImageField(upload_to='images' ,null=True)
    city = ForeignKey(City)
    country = ForeignKey(Country)


class File(models.Model):
    author = models.CharField(max_length=50,null=False)
    url = models.CharField(max_length=300,null=False)
    title = models.CharField(max_length=100,null=False)
    date = models.DateField(default=datetime.now, blank=True)
    city = ForeignKey(City)
    country = ForeignKey(Country)
    user = ForeignKey(UserGallery)
    type = ForeignKey(TypeMultimedia)
    category = ForeignKey(Category)

class FileClip(models.Model):
    name = models.CharField(max_length=50,null=False)
    secondStart = models.CharField(max_length=20,null=False)
    secondEnd = models.CharField(max_length=8,null=False)
    user = ForeignKey(UserGallery)
    file = ForeignKey(File)

class RegisterForm(ModelForm):
    class Meta:
        model = UserGallery
        fields = "__all__"

def validateEmail(self):
        email = self.cleaned_data('email')
        if UserGallery.objects.filter(email=email):
            raise forms.ValidationError('El correo electronico es unico')
        return email

