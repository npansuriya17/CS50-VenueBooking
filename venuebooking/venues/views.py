from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"venues/index.html")

def post(request, var):
    return render(request,"venues/post.html")

def find(request, var):
    
    return render(request,"venues/find.html")

def view(request, id):
    return render(request,"venues/index.html")