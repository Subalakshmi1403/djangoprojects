from django.shortcuts import render
from django.http import HttpResponse
from app.models import Bio


# Create your views here.
def index(request):
    return render(request,'index.html')