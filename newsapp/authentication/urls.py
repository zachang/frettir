from django.urls import path

from .views import RegistertView, LoginView, PasswordResetView

app_name = 'auth'
urlpatterns = [
    path('register/', RegistertView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
]