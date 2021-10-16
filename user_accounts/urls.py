from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Redirect to home page
    path('signup/', views.signup, name="signup"),  # redirect to Registration Page
    path('signin/', views.signin, name="signin"),  # redirect to Login page
    path('signout/', views.signout, name="signout"),  # Logout from the user
]