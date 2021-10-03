from django.shortcuts import render
from django.http import HttpResponse 
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')#this generator/home.html calling to home.html page
    #return HttpResponse('Hello there friend!')

def about(request):
    return render(request,'generator/about.html')#this generator/about.html calling to home.html page

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    length = int(request.GET.get('length'))# fetcing the value of password length fom the home.html

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html',{'password':thepassword} )
