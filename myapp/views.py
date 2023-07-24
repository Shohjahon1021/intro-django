from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import json

# Create your views here.
def home(request):
    return HttpResponse("Hello Djangoooo")

def about(request):
    return HttpResponse("Hello About")