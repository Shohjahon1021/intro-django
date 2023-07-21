from django.shortcuts import render

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
    pass # a, b => "result: 5"