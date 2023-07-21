from django.contrib import admin
from django.urls import path

from django.http import HttpResponse, HttpRequest


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


def hi(request, name):
    return HttpResponse(f"Hello {name}!")


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('blog/', blog),
    path('projects/', projects),

    path('sum', sum),
    path('hi/<str:name>', hi)
]
