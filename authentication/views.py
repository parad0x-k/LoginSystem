from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        userName = request.POST.get('username')
        firstName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        emailId = request.POST.get('email')
        password = request.POST.get('pass1')
        confirmPassword = request.POST.get('pass2')
    
        myUser = User.objects.create_user(userName, emailId, password)
        myUser.first_name = firstName
        myUser.last_name = lastName
    
        myUser.save()

        messages.success(request, "Your account was created succesfully")
        
        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):
    return render(request, "authentication/signin.html")

def signout(request):
    pass