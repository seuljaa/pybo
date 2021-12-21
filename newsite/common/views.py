from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm

# Create your views here.

def signup(request):
    """
    계정생성
    """
    if request.Method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()


    return