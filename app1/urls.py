from django.urls import path
from app1.views import *
app_name='new'
urlpatterns=[
    path('index/',index,name='index'),
]