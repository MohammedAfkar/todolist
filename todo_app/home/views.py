from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from home.forms import TaskForm
from home.models import Task
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
            return redirect('reg')
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


def index(request):
    tasks = Task.objects.all()
    # print(tasks)
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = TaskForm(request.POST)
            if fm.is_valid():
                fm.save()
        else:
            fm=TaskForm()
        return render(request, 'list.html', {'forms': fm, "tasks": tasks})
    else:
        return redirect('logn')
def updateTask(request, pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'update_task.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'delete.html', context)
    