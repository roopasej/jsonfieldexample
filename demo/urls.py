from django.contrib import admin
from django.urls import path,include
from demo import views

urlpatterns = [

    path('demo/',views.hello_view),
]