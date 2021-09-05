from django.urls import path
from .views import (
    home,
    postview,
    postcreate,
    postviewcreate,
    postdetail
)

urlpatterns = [
    path('', home),
    path('postview/', postview),
    path('postcreate/', postcreate),
    path('postviewcreate/', postviewcreate),
    path('postdetail/<int:pk>/', postdetail)
]