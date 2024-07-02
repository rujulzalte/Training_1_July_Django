from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request,'Login/homepage.html')

def user(request):
    return HttpResponse("User")
    
