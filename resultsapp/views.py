# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    print('inside index')
    return render(request, "index.html", )