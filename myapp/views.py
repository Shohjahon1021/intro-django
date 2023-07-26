from django.shortcuts import render
from django.http import HttpResponse, HttpRequest,JsonResponse
import json
import requests

URL = 'https://randomuser.me/api/?results=30'


def users(request: HttpRequest):
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        users = []
        photos = []
        for user in data['results']:
            users.append(user['email'])
            # photos.append(user['picture']['medium'])
        
        return JsonResponse(users, safe=False)
    
    return JsonResponse({'error':'Something went wrong'})

def photos(request: HttpRequest):
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        photos = []
        for user in data['results']:
            photos.append(user['picture']['medium'])
        
        return JsonResponse(photos, safe=False)
    
    return JsonResponse({'error':'Something went wrong'})