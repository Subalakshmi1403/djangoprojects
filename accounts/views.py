from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegisterForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegisterForm()

    return render(request,'registration/register.html',{'form':form})


def profile(request):
    return render(request,'profile.html')





def error404(request,exception):
    return render(request,'404.html')