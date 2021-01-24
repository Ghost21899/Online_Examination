from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def home_page(request):
    return render(request, 'home/base.html')