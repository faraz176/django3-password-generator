from django.shortcuts import render
from django.http import HttpResponse
import random 


def home(request):
    return render(request, 'generator/home.html', {'password': 'fidisld'})

def about(request):
    return render(request, 'generator/about.html',)

def password(request):

    #thepassword = "Nigger"

    sting = ''
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQURSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&'))

    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))
    
    length = int(request.GET.get('length'))

    for i in range(length):
        sting += random.choice(characters)

    thepassword = sting
    return render(request, 'generator/password.html', {'password': thepassword})
