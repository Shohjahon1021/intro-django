from django.contrib import admin
from django.urls import path

from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("Contact Page")

def blog(request):
    return HttpResponse("Blog Page")

def projects(request):
    return HttpResponse("Projects Page")


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('blog/', blog),
    path('projects/', projects),
]
