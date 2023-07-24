from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import json

# Create your views here.
def home(request: HttpRequest):
    params = request.GET

    name = params.get('name', 'World')

    return HttpResponse(f"Hello {name}!")

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("Contact Page")

def blog(request):
    return HttpResponse("Blog Page")

def projects(request):
    return HttpResponse("Projects Page")

def sum(request):
    data_json = request.body.decode('utf-8')
    data = json.loads(data_json)

    print(data.get('username'))
    
    return HttpResponse("Sum Page")