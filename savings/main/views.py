from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def test (request):
    return render(request, 'user/test.html', {'title': 'Test'})

def logout1 (request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'app/home.html', {'title': 'Home'})

    return render(request, 'app/home.html', {'title': 'Home'})

def home (request):
    return render(request, 'app/home.html', {'title': 'Home'})

def signin (request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'app/home.html', {'title': 'Home'})
        return render(request, 'user/signin.html', {'title': 'Sign In'})

    else:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return render(request, 'app/home.html', {'title': 'Home'})
        else:
            # No backend authenticated the credentials
            return render(request, 'user/signin.html', { 'title': 'Sign In', error: 'Invalid Credentials'})

def signup (request):
    if request.method == 'GET':
        return render(request, 'user/signup.html', {'title': 'Sign Up'})

    else:
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=email, password=password)
        return redirect('http://localhost:8000/signin')
