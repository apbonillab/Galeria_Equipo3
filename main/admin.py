from django.contrib import admin
from .models import *
# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
admin.site.register(UserGallery)
admin.site.register(File)
admin.site.register(FileClip)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(TypeMultimedia)