from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm


class RegistertView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = 'news/home.html'