
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect 
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import auth, messages
import os
from django.contrib.auth.decorators import login_required
from login_module.models import UserProfile
from django.contrib.auth.models import User
from django.urls import path, include
from login_module.facedect import dect

# Create your views here
def user_register(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid(): 
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            return HttpResponseRedirect('imgreg') 
    else: 
        form = Registrationform() 
    return render(request, 'login_module/register.html', {'form' : form})

@login_required
def user_registration_image(request):
    obj = UserProfile(user=request.user)
    
    if request.method == 'POST':
        try:
            form = RegistrationImage(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                messages.info(request, "User succesfully registered")
                auth.logout(request)
                return HttpResponseRedirect('/login')
        except:
            messages.error(request, "Error occured")
            
    else: 
        form = RegistrationImage(instance=obj) 
    
    return render(request, 'login_module/ImageRegister.html', {'form' : form})

@login_required
def user_logout(request):
    messages.info(request, 'Logged out')
    if request.user.is_authenticated:
        auth.logout(request)
    return HttpResponseRedirect('/login')

def user_login(request):
    if request.user.is_authenticated:
	    return HttpResponseRedirect('/home')
    else:
        if request.method=="POST":
            form =LoginForm(request.POST)
            if form.is_valid():
                username=request.POST['username']
                password=request.POST['password']
                try:
                    user = authenticate(request,username=username,password=password)
                    if user is not None:
                        try:
                            if user.userprofile.img:
                                face_val = dect(user.userprofile.img.url)
                                if face_val==1:
                                    login(request, user)
                                    messages.info(request, 'Logged in')
                                elif face_val==2:
                                    messages.error(request, 'Camera not found')
                                else:
                                    messages.error(request, 'Invalid user')
                            else:
                                login(request,user)
                                messages.warning(request, 'Profile Photo Not detected')
                                return HttpResponseRedirect("/imgreg")
                        except:
                            messages.error(request, 'No faces Detected')
                        return HttpResponseRedirect('/home')
                except:
                    messages.error(request, 'Error Authenticating user')
                    return HttpResponseRedirect('/login')
        else:
            form = LoginForm()
        return render(request, 'login_module/login.html', {'form': form})