from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect 
from .forms import *

# Create your views here
def user_login():
    pass

def user_register(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('imgreg') 
    else: 
        form = Registrationform() 
    return render(request, 'login_module/register.html', {'form' : form})

def success(request): 
    return HttpResponse('successfully Registered')

def user_registration_image(request):
    if request.method == 'POST':
        form = RegistrationImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else: 
        form = RegistrationImage() 
    return render(request, 'login_module/ImageRegister.html', {'form' : form})