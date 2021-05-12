from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import face_recognition
import cv2 
import os

# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        if str(request.user.userprofile.img) == "":
            return HttpResponseRedirect('../logout/')
        return render(request, 'home/base.html')
    else:
        return HttpResponseRedirect('../login/')