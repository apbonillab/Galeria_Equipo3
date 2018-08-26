from django.conf.urls import  url

from main import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/(\d+)/$', views.register, name='register_upd'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logoutsession, name='logout')

]
