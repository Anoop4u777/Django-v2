from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def items(request):
    return HttpResponse("<h1>This is an item view.</h1>")