from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def base(request):
    return render(request,"Portfolio/base.html")
def projects(request):
    return render(request,"Portfolio/projects.html")
def home(request):
    return render(request, "Portfolio/home.html")