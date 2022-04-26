from dataclasses import fields
from ideaBoatApp1 import views
from .models import Post,Post_Category, PostLikes,Comment

from rest_framework import  serializers
from django.contrib.auth.models import User
class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = '__all__'
class Post_CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Post_Category
        fields = '__all__'   
class PostLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = PostLikes
        fields = '__all__' 
        
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = '__all__' 