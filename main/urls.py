from django.conf.urls import  url

from main import views
from main.views import FileAPI

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/(\d+)/$', views.register, name='register_upd'),
    url(r'^login/$', views.loginsession, name='login'),
    url(r'^agregar_clip/$', views.agregar_clip, name="agregar_clip"),
    url(r'^logout/$', views.logoutsession, name='logout'),
    url(r'^findbycategory/$', views.findbycategoria, name='findbycategory'),
    url(r'^findbytype/$', views.findfilebytypemultimedia, name='buscar_archivo_por_tipo_multimedia'),
    url(r'^api/$', FileAPI.as_view(), name='api'),
    url(r'^ingreso/$', views.ingreso, name='ingreso')

]
