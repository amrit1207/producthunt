from django.shortcuts import render

def home(request):
    return render(request,'product/home.html')


def create(request):
    return render(request,'product/create.html',)