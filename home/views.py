from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        return render(request, 'home/base.html')
    else:
        return HttpResponseRedirect('../login/')
    