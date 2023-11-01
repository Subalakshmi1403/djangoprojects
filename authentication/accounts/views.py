from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm , EditProfileForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = RegistrationForm()
    return render(request,'registration/signup.html',{'form':form})
@login_required
def profile(request):
    return render(request,'profile.html')
@login_required
def EditProfile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts/profile')
    else:
        form = EditProfileForm()
    return render(request,'edit_profile.html',{'form':form})



# Create your views here.
