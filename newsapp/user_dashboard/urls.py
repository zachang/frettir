from django.urls import path

from .views import UserDashboard

app_name = 'user_dashboard'
urlpatterns = [
    path('profile/', UserDashboard.as_view(), name='profile'),
]