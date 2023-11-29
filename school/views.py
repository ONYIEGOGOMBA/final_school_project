from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = name
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Account created successful")

        return redirect('signin')







    return render(request, 'index.html')

def signup(request):
    return render(request, 'index.html/#signup-section')

def signin(request):
    return render(request,'index.html/contact-section')

def signout(request):
    pass