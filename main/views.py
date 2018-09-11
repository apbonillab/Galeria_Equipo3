# -*- coding: utf-8 -*-
import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.serializers import serialize

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers

from main.models import RegisterForm, File, FileClip, UserGallery, Category
from main.serializers import FileSerializer


def index(request):
    print('main')
    brands_list = [];
    lista_multimedia = File.objects.all();
    for l in lista_multimedia:
        lista_clips = FileClip.objects.filter(file_id=l.id);
        context = {'clip': lista_clips, "title": l.title, "id": l.id, "author": l.author, "date": l.date, "url": l.url}
        brands_list.append(context);
    context = {'multimedia': brands_list}
    return render(request, 'main/index.html', context)


def register(request, value=None):
    title = "Confirmación de creación";
    body = "La cuenta se creo exitosamente";
    if request.user.is_authenticated:
        title = "Confirmación de actualización";
        body = "La cuenta se actualizo exitosamente";
    if '2' == value:
        us = UserGallery.objects.filter(user_session=request.user)
        for l in us:
            context = {'user_session': l.user_session, 'name': l.name, "email": l.email, "password": l.password,
                       "image": l.image,
                       "city": l.city, "country": l.country, "upd": 'true'}
        form = RegisterForm(instance=UserGallery, initial=context);
        form.fields['email'].widget.attrs['readonly'] = True;
        form.fields['password'].widget.attrs['readonly'] = True;
        form.fields['user_session'].widget.attrs['readonly'] = True;
        return render(request, 'main/register.html', {'form': form})

    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save();
                email = EmailMessage(title, body, to=[request.POST.get('email')]);
                email.send();
                if request.user.is_authenticated:
                    user = authenticate(username=request.POST.get('user_session'),
                                        password=request.POST.get('password'))
                    if user is not None:
                        login(request, user);
                    return HttpResponseRedirect(reverse('main:index'))
                else:
                    user_model = User.objects.create_user(request.POST.get("user_session"), request.POST.get("email"),
                                                          request.POST.get("password"));
                    user_model.save();
                    user = authenticate(username=request.POST.get('user_session'),
                                        password=request.POST.get('password'))
                    if user is not None:
                        login(request, user);
                    return HttpResponseRedirect(reverse('main:index'))

            else:
                return render(request, 'main/register.html', {'form': form})
        else:
            form = RegisterForm()
            return render(request, 'main/register.html', {'form': form})


def preloadUser(request):
    user = User.objects.filter(user=request.POST.get('user'));
    return render(request, 'main/index.html', user)

@csrf_exempt
def loginsession(request):
    if request.method == 'POST':
            jsondata = json.loads(request.body)
            username = jsondata['username']
            password = jsondata['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user);
                mensaje='ok'
            else:
                mensaje = 'Datos incorrectos'
    return JsonResponse({'mensaje': mensaje})

@csrf_exempt
def isAuthenticated(request):
    if request.user.is_authenticated():
        mensaje='ok'
    else:
        mensaje='fail'
    return JsonResponse({'mensaje':mensaje})

def logoutsession(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def agregar_clip(request):
    agregar_clip = FileClip()
    if request.method == 'POST':
        name = request.POST.get('name')
        secondStart = request.POST.get('secondStart')
        secondEnd = request.POST.get('secondEnd')
        fileId = request.POST.get('fileId')
        agregar_clip.name = name
        agregar_clip.secondStart = secondStart
        agregar_clip.secondEnd = secondEnd
        agregar_clip.file = File.objects.get(pk=fileId)
        agregar_clip.user = UserGallery.objects.get(pk=10)
        agregar_clip.save()
        return HttpResponseRedirect(reverse('main:index'))


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def findbycategoria(request):
    template_name = 'main/findbycategory.html'
    if File.objects.filter(category_id=request.GET.get('categoryName')).exists():
        lista_multimedia = File.objects.filter(category_id=request.GET.get('categoryName'));
        context = {'multimedia': lista_multimedia}
        data = {'lista_multimedia': lista_multimedia}
        return Response(data, template_name='main/findbycategory.html')
        #return JsonResponse({'lista_multimedia': serialize('json', lista_multimedia)}, template_name='main/findbycategory.html')
    else:
        return render(request, template_name)


def findfilebytypemultimedia(request):
    template_name = 'main/findByType.html'
    brands_list = [];
    if File.objects.filter(typemultimedia__name=request.GET.get('typeName')).exists():
        lista_multimedia = File.objects.filter(typemultimedia__name=request.GET.get('typeName'));
        for l in lista_multimedia:
            lista_clips = FileClip.objects.filter(file_id=l.id);
            context = {'clip': lista_clips, "title": l.title, "id": l.id, "author": l.author, "date": l.date,
                       "url": l.url}
            brands_list.append(context);
        context = {'multimedia': brands_list}
        return render(request, 'main/findByType.html', context)
    else:
        return render(request, template_name)


class FileAPI(APIView):
    serializer=FileSerializer

    def get(self,request,format=None):
        lista=File.objects.all()
        response=self.serializer(lista,many=True)

        return HttpResponse(json.dumps(response.data),content_type='application/json')
@csrf_exempt
def ingreso(request):
    print ('b')
    return render(request,'main/login.html')