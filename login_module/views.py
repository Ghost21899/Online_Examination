
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect 
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import auth, messages
import os
from django.contrib.auth.decorators import login_required
from login_module.models import UserProfile
from django.contrib.auth.models import User
from cv2 import cv2 
import face_recognition
from django.urls import path, include

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
                return HttpResponseRedirect('/logout')
        except:
            pass
            
    else: 
        form = RegistrationImage(instance=obj) 
    
    return render(request, 'login_module/ImageRegister.html', {'form' : form})

@login_required
def user_logout(request):
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
                                if facedect(user.userprofile.img.url):
                                    login(request, user)
                                    messages.info(request, 'Logging in')
                                else:
                                    messages.error(request, 'Invalid user')
                            else:
                                login(request,user)
                                messages.warning(request, 'Profile Photo Not detected')
                                return HttpResponseRedirect("/imgreg")
                            
                        except Exception as e:
                            print(e)
                            messages.error(request, 'No faces Detected')
                            #login(request,user)
                            #return HttpResponseRedirect("/imgreg")
                        return HttpResponseRedirect('/home')
                except:
                    messages.error(request, 'Error Authenticating user')
                    return HttpResponseRedirect('/login')
        else:
            form = LoginForm()
        return render(request, 'login_module/login.html', {'form': form})

    
def facedect(loc):
    cam = cv2.VideoCapture(0) 
    cam.set(3, 1280)
    cam.set(4, 720)
    for i in range(30):
        temp = cam.read()  
    s, img = cam.read()
    if s:   
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MEDIA_ROOT = os.path.join(BASE_DIR, '') 
        loc = (str(MEDIA_ROOT)+str(loc))
        print(loc)
        
        face_1_image = face_recognition.load_image_file(loc)
        face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]
        
        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        check=face_recognition.compare_faces(face_1_face_encoding, face_encodings)
        
        print(check)
        if check[0]:
            return True
        else :
            return False  