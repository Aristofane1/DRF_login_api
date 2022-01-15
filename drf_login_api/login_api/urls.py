from django.urls import path
from .views import *
from rest_framework.authtoken import views

urlpatterns = [
    path('register/', RegisterView.as_view(), name="registration"),
    path('login/', views.obtain_auth_token, name="login"),
    path('home/', UserView.as_view(), name="home"),
]