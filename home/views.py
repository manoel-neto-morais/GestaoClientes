from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')


def mylogout(request):
    logout(request) #função interna do django para efetuar o logout
    return redirect('home')


