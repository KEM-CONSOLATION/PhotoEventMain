from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.core.validators import RegexValidator
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone','norsical', 'patrol', 'designation', 'Do_You_Use_Hard_Drugs','passport']



class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields=("amount","email",)