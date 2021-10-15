from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'index.html')
