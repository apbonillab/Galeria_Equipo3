# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse

from main.models import RegisterForm, User


def index(request):

    context = {'lista_imagenes' : 'fllala'}
    return render(request,'main/index.html',context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))

    else:
        form = RegisterForm()
        return render(request, 'main/register.html', {'form':form})

def login(request):
    mensaje = ''
    if request.user.is_authenticated():
        return redirect(reverse('main:index'))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            print (user)
            if user is not None:
                return redirect(reverse('main:index'))
            else:
                mensaje = 'Datos incorrectos'
    return render(request, 'main/login.html', {'mensaje':mensaje})

def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))