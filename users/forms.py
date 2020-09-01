from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Update
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

#Delete
class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []   #Form has only submit button.  Empty "fields" list still necessary, though.