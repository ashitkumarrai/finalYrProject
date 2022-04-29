from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import  serializers,generics
from ideaBoatApp1 import serializers
from ideaBoatApp1.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from .models import Post,Comment,PostLikes,Post_Category
from rest_framework.permissions import IsAdminUser
from rest_framework import views




class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class RegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()

    serializer_class = serializers.RegisterSerializer















class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# ----------------------------------------------------------------------------------------------------------------------------------------


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


# ----------------------------------------------------------------------------------------------------------------------------------------
class LikeList(generics.ListCreateAPIView):
    queryset = PostLikes.objects.all()
    serializer_class = serializers.PostLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,)
class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =PostLikes.objects.all()
    serializer_class = serializers.PostLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]




# ----------------------------------------------------------------------------------------------------------------------------------------# ----------------------------------------------------------------------------------------------------------------------------------------
class CategoryList(generics.ListCreateAPIView):
    queryset = Post_Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_Category.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


