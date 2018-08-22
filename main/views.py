# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.shortcuts import render
# Create your views here.
def index(request):

    context = {'lista_imagenes' : 'fllala'}
    return render(request,'main/index.html',context)

