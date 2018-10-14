from django.urls import path

from .views import RegistertView, LoginView

app_name = 'auth'
urlpatterns = [
    path('register/', RegistertView.as_view()),
    path('login/', LoginView.as_view()),
]