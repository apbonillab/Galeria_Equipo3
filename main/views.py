# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse

from main.models import RegisterForm, File, FileClip, User


def index(request):
        brands_list = [];
        lista_multimedia = File.objects.all();
        for l in lista_multimedia:
            lista_clips = FileClip.objects.filter(file_id=l.id);
            print lista_clips.values();
            context = {'clip': lista_clips,"title":l.title,"id":l.id,"author":l.author ,"date":l.date, "url":l.url}
            brands_list.append(context);
        context = {'multimedia' : brands_list}
        return render(request,'main/index.html', context)


def register(request,value=None):
    title = "Confirmación de creación";
    body = "La cuenta se creo exitosamente";
    if request.user:
        title = "Confirmación de actualización";
        body = "La cuenta se actualizo exitosamente";
    if '2'==value:
        print "iguales";
        us = User.objects.filter(email='apbonillab@gmail.com')
        form = RegisterForm(instance=User,initial={'name':'adriana'});
        for l in us:
            print  l.name;
            context = {'name': l.name, "email": l.email, "category": l.category, "password": l.password, "image": l.image,
                       "city": l.city,"country": l.country,"upd":'true'}
        form = RegisterForm(instance=User, initial=context);
        form.fields['email'].widget.attrs['readonly'] = True;
        form.fields['password'].widget.attrs['readonly'] = True;
        print form;
        return render(request, 'main/register.html', {'form': form})

    else:
        if request.method == 'POST':
            print 'hara actualizacion-creacion';
            form = RegisterForm(request.POST,request.FILES)
            if form.is_valid():
                form.save();
                email = EmailMessage(title,body, to=[request.POST.get('email')]);
                email.send()
                if request.user:
                    return HttpResponseRedirect(reverse('main:index'))
                else:
                    user_model = User.objects._create_user(request.POST.get("email"),request.POST.get("email"),request.POST.get("password"));
                    user_model.save();
                    return HttpResponseRedirect(reverse('main:index'))

            else:
                return render(request, 'main/register.html', {'form': form})
        else:
            form = RegisterForm()
            return render(request, 'main/register.html', {'form':form})

def preloadUser(request):
    user = User.objects.filter(user=request.POST.get('user'));
    return render(request,'main/index.html', user)

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

def logoutsession(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))