from django.shortcuts import render,  redirect
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .forms import RegisterForm, LoginForm, PasswordResetForm


class RegistertView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        username = self.request.POST.get('username')
        first_name = self.request.POST.get('first_name')
        last_name = self.request.POST.get('last_name')
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        confirm_password = self.request.POST.get('password_conf')

        user = User(username=username, first_name=first_name, 
        last_name=last_name, email=email)
        lookup_user = User.objects.filter(Q(email=email) | Q(username=username))
        if not lookup_user:
            user.set_password(password)
            user.save()
            auth_user = authenticate(username=username, password=password)
            login(self.request, auth_user)
            return redirect('/')
        messages.error(self.request, 'This email or username already exist')
        return HttpResponseRedirect(reverse('auth:register'))

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    
    def form_valid(self, form):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        auth_user = authenticate(username=username, password=password)

        if auth_user:
            login(self.request, auth_user)
            return redirect('/')
        messages.error(self.request, 'The username or password is incorrect')
        return HttpResponseRedirect(reverse('auth:login'))
        

class PasswordResetView(FormView):
    template_name = 'password_reset.html'
    form_class = PasswordResetForm
    success_url = 'news/home.html'