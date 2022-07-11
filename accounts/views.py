from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView)
from . models import CustomUser
from . forms import CustomUserCreationForm,CustomUserChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
class Signup(CreateView):
    model = CustomUser
    password = forms.CharField(widget=forms.PasswordInput)
    fields = ("first_name", "last_name", "email", "phone", "password")
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'

