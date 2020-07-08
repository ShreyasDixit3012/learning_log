# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:17:10 2020

@author: Shreyas Dixit
"""


"""Defines URL patterns for users"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout page
    path('logout/', views.logout_view, name='logout'),
    # Registration Page
    path('register/', views.register, name='register'),
    #Welcome page
    path('welcome/',views.welcome, name='welcome')
    ]