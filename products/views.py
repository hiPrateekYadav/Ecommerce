from django.shortcuts import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Home page")


def favourite(request):
    return render(request, "home.html")
