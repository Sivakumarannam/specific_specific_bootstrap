from django.urls import path
from app2.views import *
app_name='hello'
urlpatterns=[
    path('index1/',index1,name='index1'),
]