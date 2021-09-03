from django.shortcuts import render
# from rest_framework import api_view
# from rest_framework import Response
from rest_framework import status
from .serializers import PostSerializer
from django.http import HttpResponse

def post_list(request):
    return HttpResponse('<center><h1>welcome to post</h1><center>')
