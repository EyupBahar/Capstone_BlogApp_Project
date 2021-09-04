from django.shortcuts import render
from rest_framework import api_view
from rest_framework import Response
from rest_framework import status
from .serializers import PostSerializer
from django.http import HttpResponse
from rest_framework.views import APIView

def post_list(request):
    return HttpResponse('<center><h1>welcome to post</h1><center>')

class

def  get(self,request):
    queryset = Posts.object.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)

def post(self,request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 