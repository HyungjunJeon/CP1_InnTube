from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return render(request,'testapp/hi.html')

def create(request):    
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read'+ id)