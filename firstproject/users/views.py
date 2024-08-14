from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def register_user(req):
  if req.method == "POST":
    form = UserCreationForm(req.POST)
    if form.is_valid():
      login(req,form.save()) # this also returns the user so its valid
      return redirect("posts:list")
  else:
    form = UserCreationForm()
  
  return render(req,'users/register.html',{'form':form})

def login_user(req):
  if req.method =="POST":
    form = AuthenticationForm(data=req.POST)
    if form.is_valid():
      login(req,form.get_user())
      if 'next' in req.POST:
        return redirect(req.POST.get('next'))
      else:
        return redirect("posts:list")
  else:
    form = AuthenticationForm()
  
  return render(req,'users/login.html',{'form':form})

def logout_user(req):
  if req.method == "POST":
    logout(req)
    return redirect("posts:list")