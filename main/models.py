# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models import ForeignKey


class City(models.Model):
    name = models.CharField(max_length=50, null=False)

class Country(models.Model):
    name = models.CharField(max_length=50, null=False)

class TypeMultimedia(models.Model):
     name = models.CharField(max_length=50, null=False)
     description = models.CharField(max_length=500, null=True)

class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=500, null=True)

class User(models.Model):
    name = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=20,null=False)
    password = models.CharField(max_length=8,null=False)
    image = models.ImageField(upload_to='images' ,null=True)
    city = ForeignKey(City)
    country = ForeignKey(Country)
    category = ForeignKey(Category, null=True)

class File(models.Model):
    author = models.CharField(max_length=50,null=False)
    url = models.CharField(max_length=20,null=False)
    title = models.CharField(max_length=8,null=False)
    date = models.ImageField(upload_to='images' ,null=True)
    city = ForeignKey(City)
    country = ForeignKey(Country)
    user = ForeignKey(User)
    category = ForeignKey(Category)

class FileClip(models.Model):
    name = models.CharField(max_length=50,null=False)
    secondStart = models.CharField(max_length=20,null=False)
    secondEnd = models.CharField(max_length=8,null=False)
    user = ForeignKey(User)
    file = ForeignKey(File)



