from django.shortcuts import render

# Create your views here.
def start_exam(request):
    return render(request, 'monitor/exam.html')