from operator import index
from django.urls import URLPattern, path
from . import views


urlpatterns =[
    path('', views.index, name= 'index'),  #the name index here is the name of the fun defined in views file. 
]