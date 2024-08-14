# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  # return HttpResponse("You're on the home page...")
  return render(request,'home.html')

def about(request):
  # return HttpResponse("You're on the about page...")
  return render(request,'about.html')