from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login


# Create your views here.
def welcome(request):
    return render(request,"MyApp/welcome.html")

def welcome(request):
    return render(request,"MyApp/welcome.html")

def register(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request,'registration/register.html',{"form":form})
    else:
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
        else:
            return HttpResponse("Error")
        return redirect("/")
