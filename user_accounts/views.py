from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .password_validation import password_checking
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail


def home(request):
    if request.user.is_authenticated:
        return redirect(reverse('products'))
    else:
        return render(request, "accounts/index.html")


def signup(request):
    if request.user.is_authenticated:
        return render(request, "accounts/index.html")

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        returned_error_response = password_checking(password)
        user = User.objects.filter(username=username)
        # print(len(user))
        # Username checking from database
        if len(user) != 0:
            temp = {"username_checking": "Username is already exists."}
            returned_error_response.update(temp)

        # If Password is meets with password validations then create user object
        if len(returned_error_response) == 0:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            login(request, user)
            # messages.success(request, 'You Have Been Logged In!')

            # welcome mail send
            subject = 'Welcome to eComAssesment'
            details = 'Dear User,\n\n' + 'Username : ' + username + 'has been registered to eComAssemement.'

            body = "\n\nPlease keep your username and password confidential.\n\n\nBest Wishes,\nMr. X\nHead of " \
                   "Operations,\nThe ITQAN Analytics & Software Limited. "
            send_mail(
                subject,
                details + body,
                settings.EMAIL_HOST_USER,
                [email]
            )
            return redirect(reverse('products'))
        else:
            temp = {"username": username, "email": email}
            returned_error_response.update(temp)
            return render(request, template_name="accounts/signup.html", context=returned_error_response)
    return render(request, 'accounts/signup.html')


def signin(request):
    if request.user.is_authenticated:
         return render(request, "products/products.html")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, 'You Have Been Logged In!')
            return redirect(reverse('products'))
        else:
            return render(request, 'accounts/signin.html', {'messages': 'Wrong Credential'})
    else:
        return render(request, 'accounts/signin.html', {'messages': ''})


def signout(request):
    logout(request)
    return redirect(home)