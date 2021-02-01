import json
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect
from django.core.serializers import serialize
from django.urls import reverse
from rest_framework import viewsets
from .serializers import ArtistsSerializer, GenreSerializer, ShowsSerializer, VenuesSerializer
from .models import Artist, Genre, Shows, Venues

# Create your views here.
def index(request):
    return render(request,"venues/index.html")

def post(request, var):
    return render(request,"venues/post.html")

def find(request, var):
    if var == "shows":
        shows = Shows.objects.all()
        

    return render(request,"venues/find.html")

def view(request):
    return render(request,"venues/index.html")

def lists(request, var):
    if request.method != "POST":
        if var == "shows":
            items = Shows.objects.all()
        elif var == "venues":
            items = Venues.objects.all()
        elif var == "artists":
            items = Artist.objects.all()
        else:
            return JsonResponse({"error": "Invalid details."}, status=400)
        print(items)
        return JsonResponse(serialize('json',items),safe=False)


def list_item(request, id):
    return True

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)