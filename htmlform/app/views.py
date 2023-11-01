from django.shortcuts import render
from app.models import htmlform

# Create your views here.
def index(request):
    if request.method == "POST":
        if request.POST.get('title') and request.POST.get('body'):
            html = htmlform()
            html.title= request.POST.get('title') 
            html.body = request.POST.get('body')
            html.save()
    return render(request,'index.html')
