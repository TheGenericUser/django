from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, loader, redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse('This is home page')

def about(request):
    return HttpResponse('This is about page')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['cpassword']

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(request, "You account is created.")
        return redirect('signin')

    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=username, email=email, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.error(request, "Wrong details")
            return redirect('signin')

    return render(request, 'signin.html')