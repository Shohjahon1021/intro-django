from django.urls import path
from .views import users,photos


urlpatterns = [
    path('users/',users),
    path('photos/',photos)
]

