from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from . forms import texts

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('logn')

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
            messages.info(request,"invalid login")
            return redirect('logn')
    else:
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request,"login.html")

def register(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken")  
            return redirect('reg')
        else:  
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
        return redirect('logn')
    else:
        return render(request,"register.html")
    
def logout(request):
    auth_logout(request)
    return redirect('logn') 

from . models import todo_text

def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = texts(request.POST)
            if fm.is_valid():
                fm.save()
        else:
            fm=texts()
        tex = todo_text.objects.all()
        return render(request, 'index.html', {'forms': fm, "tex": tex})
    else:
        return redirect('logn')
    