from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) :
    return HttpResponse("Home page")

def favourite(request) :
    return HttpResponse("fovourite page")