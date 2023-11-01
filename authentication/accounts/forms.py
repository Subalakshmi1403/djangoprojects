from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm , UserChangeForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'email',
            'username',
        }
        def save(self,commit = True):
            user = super(RegistrationForm,self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.username = self.cleaned_data['username']
            if commit:
                user.save()
            return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'email',
        }