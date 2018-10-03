from django.urls import path

from .views import HomePageView

app_name = 'news'
urlpatterns = [
    path('home/', HomePageView.as_view()),
]