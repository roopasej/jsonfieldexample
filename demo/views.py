from django.shortcuts import render

from .models import Language

def hello_view(request):
    print('hi')
