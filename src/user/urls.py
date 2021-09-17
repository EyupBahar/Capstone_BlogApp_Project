from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import CustomAuthToken, register_view, logout_view

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    path('register/', register_view),
    path('logout/', logout_view),
]   