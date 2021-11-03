from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all() # grab everything related to the project from the database
    return render(request,'portfolio/home.html',{'projects':projects})
