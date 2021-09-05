from django.urls import path
from .views import (
    home,
    # postview,
    # postcreate,
    # postviewcreate,
    # postdetail,
    PostListCreateAPIView
)

urlpatterns = [
    path('', home),
    # path('postview/', postview),
    # path('postcreate/', postcreate),
    path('postviewcreate/', PostListCreateAPIView.as_view()),
    # path('postdetail/<int:pk>/', postdetail),
    # path('PostListCreateAPIView/<int:pk>/', PostListCreateAPIView)
]