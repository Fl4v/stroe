from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def thank_you(request):
    return render(request, 'thank_you.html')


def handler404(request, exception):
    return render(request, '404.html')
