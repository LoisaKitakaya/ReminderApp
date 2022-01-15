from django.http import response
from django.shortcuts import render
import requests

# Create your views here.
def home(request):

    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        'x-rapidapi-host': "quotes15.p.rapidapi.com",
        'x-rapidapi-key': "53261179d3msh4f625af6c821a4cp17aaa5jsn475301ddb7c1"
        }

    response = requests.request("GET", url, headers=headers)

    response = response.json()

    print(response)

    context = {
        'quote' : response
    }

    return render(request, 'home.html', context)

def app(request):

    return render(request, 'app/index.html')