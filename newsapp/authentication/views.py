from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm, PasswordResetForm


class RegistertView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = 'news/home.html'

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = 'news/home.html'

class PasswordResetView(FormView):
    template_name = 'password_reset.html'
    form_class = PasswordResetForm
    success_url = 'news/home.html'