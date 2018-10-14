from django.urls import path

from .views import RegistertView

app_name = 'auth'
urlpatterns = [
    path('register/', RegistertView.as_view()),
]