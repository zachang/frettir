from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """This renders the home page"""
    template_name = 'news/home.html'
