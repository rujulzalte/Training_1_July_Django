from django.shortcuts import render
from django.http import HttpResponse
from . models import User
# Create your views here.

def homepage(request):
    return render(request,'Login/homepage.html')

def user(request):
    return HttpResponse("User")
    
def index(request):
    all_objects = User.objects.all()
    print(all_objects)
    return render(request, 'Login/index.html', {'User': all_objects})