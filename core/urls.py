from django.contrib import admin
from django.urls import path

from django.http import HttpResponse, HttpRequest



from myapp.views import home, about, contact, blog, projects, sum

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
