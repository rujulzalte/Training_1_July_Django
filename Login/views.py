from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import User
from . serializers import UserSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def homepage(request):
    return render(request,'Login/homepage.html')

def user(request):
    return HttpResponse("User")
    
def index(request):
    all_objects = User.objects.all()
    print(all_objects)
    return render(request, 'Login/index.html', {'User': all_objects})

@csrf_exempt
def alldetails(request):
    try:
        all_data = User.objects.all()
    except Exception as e:
        print(e)
        return HttpResponse("Sorry!!!Not Found", status = 404)
    
    if request.method == 'GET':
        user = UserSerializer(all_data, many = True)
        return JsonResponse(user.data, safe = False)
    
    elif request.method == 'POST':
        input_data = JSONParser().parse(request)
        serializer = UserSerializer(data = input_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        else:
            return HttpResponse("Error!!!Invalid Data", status = 400)
@csrf_exempt     
def singleuser(request,pk):
    try:
        data = User.objects.get(pk=pk)
    except:
        return HttpResponse("Sorry!!!Not Found", status = 404)
    
    if request.method == 'GET':
        user = UserSerializer(data)
        return JsonResponse(user.data, status=200, safe = False)
    
    elif request.method == 'PUT':
        new_data = JSONParser().parse(request)
        serializer = UserSerializer(data,data=new_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        else:
            return HttpResponse("Error!!!Invalid Data", status = 400)
        
    elif request.method == 'DELETE':
        data.delete()
        return HttpResponse("Done", status = 204)