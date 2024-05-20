from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request=request, template_name="homepage.html")

def coverpage(request):
    return render(request=request, template_name="coverpage.html")

def signin(request):
    user_name = request.POST.get("Name")
    pwd = request.POST.get("pass1")
        
    if request.method == "POST":
        user = authenticate(request=request, username=user_name, password=pwd)
        
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request=request,
                        message="please Register Yourself !")

    return render(request=request, template_name="signin.html")

def register(request):
    username = request.POST.get("Name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    password = request.POST.get("pass1")
    confirm_pwd = request.POST.get("pass2")

    if request.method == "POST":

        if User.objects.filter(username=username).exists():
            messages.error(request=request, message="User Already Registered")
        
        elif password != confirm_pwd:
            messages.error(request=request, message="Password and confirm password is not matching")
        
        elif len(phone) != 10:
            messages.error(request=request, message="Please enter valid mobile number")
        else:
            user = User.objects.create_user(username=username , email = email,  password=password)
            user.save()
            return redirect("signin")

    return render(request=request, template_name="Register.html")

def signout(request):
    logout(request=request)
    return redirect("signin")