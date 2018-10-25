from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import UpdateForm


class UserDashboard(FormView):
    """This renders the user dashboard page"""
    template_name = 'dashboard.html'
    form_class = UpdateForm
    success_url = 'news/home.html'