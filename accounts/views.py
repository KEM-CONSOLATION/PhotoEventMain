from django.http import HttpResponse
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect,render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from . import forms
from .forms import MyUserCreationForm, ProfileEditForm
from django.conf import settings



# Create your views here.
def home(request):
    return render(request,'home.html')

def event(request):
    return render(request,'dashboard.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/checkout/')
    else:
        form = MyUserCreationForm()
        if request.method == 'POST':
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user=form.save()
                
                # Create the user profile
                profile = Profile.objects.create(user=user)
                
                username=form.cleaned_data.get('username')
                return redirect('/checkout/')
        
        context={'form':form}
    return render(request,'register.html',context)

@login_required(login_url='login')
def edit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
       
        profile_form = ProfileEditForm(instance=request.user.profile)
        return redirect('dashboard')
        
    context={'profile_form': profile_form}

    return render(request,'account_settings.html',context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('checkout')
                      
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request,'login.html')


def logoutUser(request):
	logout(request)
	return redirect('login')


def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        payment_form=forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            
            payment=payment_form.save()
            return render(request,'makepayment.html',{'payment':payment,'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form=forms.PaymentForm()
    return render(request,'checkout.html',{'payment_form':payment_form})

@login_required(login_url='login')
def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified=payment.verify_payment()
    if verified:
        messages.success(request, "Verification Successfull")
    else:
        messages.error(request,"Verification Failed")
    return render(request,'account_settings')

