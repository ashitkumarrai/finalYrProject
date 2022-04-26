from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User

from django.shortcuts import render
from rest_framework import  serializers,generics
from ideaBoatApp1 import serializers

from .models import Post,Comment,PostLikes

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# -------------------------------------------------------


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]



class LikeListCreate(generics.ListCreateAPIView):
    queryset = PostLikes.objects.all()
 

    def get(self,request,pk):#function to get total number of likes to particular post
        post = Post.objects.filter(pk=pk) # find which post's likes are to be extracted
        like_count = Post.like_count(pk)
        serializer = serializers.PostLikeSerializer(like_count,many=True)
        return Response(serializer.data)


# def post(self,request,pk):
#     likeusers = User.objects.get(id=pk)
#     likepost = Post.objects.filter(pk=pk)
#     check = PostLikes.objects.filter(Q(likeusers=like_user) & Q(likepost = likepost.last() ))
#     if(check.exists()):
#         return Response({
#             "status": status.HTTP_400_BAD_REQUEST,
#             "message":"Already Liked"
#             })
#     new_like = PostLikes.objects.like(likeusers=likeusers, likepost=likepost.last())
#     new_like.save()
#     serializer = serializers.PostLikeSerializer(new_like)
#     return Response(serializer.data,status=status.HTTP_201_CREATED)