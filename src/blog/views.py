from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .pagination import SmallPagination, LargePagination
from django_filters.rest_framework import DjangoFilterBackend 


def home(request):
    return HttpResponse('<center><h1>welcome to post</h1><center>')


class PostListCreateAPIView(generics.ListCreateAPIView):

    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer

    pagination_class = SmallPagination
    filterset_fields = ['category',]
    # search_fields = ['title','content', "author__authorname"]
    # ordering_fields = ['publish_date', "title", "author" ]

    # def create(self, **kwargs):
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostList(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
#     filterset_fields = ['category']
#     # search_fields = ['title','content', "author__authorname"]
#     ordering_fields = ['publish_date', "title", "author" ]

# class PostCreate(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
    
#     def create(self, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
# class PostListCreateAPIView(ListModelMixin, CreateModelMixin,GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request):
#         return self.list(request, *args, **kwargs)



# @api_view(['GET'])
# def postview(request):
#     queryset = Post.objects.all()
#     serializer = PostSerializer(queryset, many=True)
#     return Response(serializer.data)

# @api_view(['POST    '])
# def postcreate(request):
#     serializer = PostSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# @api_view(['GET', 'POST'])
# def postviewcreate(request):
#     if request.method == 'GET':
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT','DELETE'])
# def postdetail(request, pk):
    # try:
    #     post = Post.objects.get(pk=pk)

    # except Post.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
    # if request.method == 'GET':
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)

    # elif request.method == 'PUT':
    #     serializer = PostSerializer(post, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'DELETE':
    #     post.delete ()
    #     return Response(status=status.HTTP_204_NO_CONTENT)