import requests
from django.shortcuts import render

# Create your views here.

def home(request):
    context = get_data_from_jason('https://cefis.com.br/api/v1/event')
    return render(request, 'index.html', context)

def view_detail(request, id):
    context = get_data_from_jason('https://cefis.com.br/api/v1/event/'+str(id)+'?include=classes')
    return render(request, 'curso.html', context)

def get_data_from_jason(url):
    response = requests.get(url)
    return response.json()