from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'todo.html')
        
        e = 'Invalid Username or Password'
        return render(request, 'index.html', {'message': e})
    
    return render(request, 'index.html')

@login_required
def todo(request):
    return render(request, 'todo.html')

@login_required
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        to_do = request.POST.get('to_do')
        User.objects.create(name=name, desc=desc, to_do=to_do, date=date)
        return render(request, 'todo.html', {'message': 'Saved Successfully !!'})
    return render(request, 'create.html')

@login_required
def signout(request):
    logout(request)
    return redirect(index)

@login_required
def users(request):

    if not User.objects.all():
        return render(request, 'users.html', {'message': 'No User Found !!'})
    
    users = User.objects.all()
    return render(request, 'users.html', {'ALL': users})

@login_required
def details(request, id):
        
    user = User.objects.get(id=id)
    details = user.to_do.split('\n')
    return render(request, 'user_details.html', {'i': user, 'x': details})

@login_required
def delete_todo(request, id):
    try:
        user = User.objects.get(id=id)
        name = request.POST.get('name')
        name = user.name
    except User.DoesNotExist:
        messages.error(request, 'User not found.')
        return redirect('users')

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully')
        return redirect('users')

    return render(request, 'delete.html', {'id': id, 'name':name})
