
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from ideaBoatApp1 import views



urlpatterns = [
    path('api/users/', views.UserList.as_view()),
    path('api/users/<int:pk>/', views.UserDetail.as_view()),

    path('admin/', admin.site.urls),


    path('api/posts/', views.PostList.as_view()),
    path('api/posts/<int:pk>/', views.PostDetail.as_view()),

    path('api/comments/', views.CommentList.as_view()),
    path('api/comments/<int:pk>/', views.CommentDetail.as_view()),


    path('api/categories/', views.CategoryList.as_view()),
    path('api/categories/<int:pk>/', views.CategoryDetail.as_view()),




    path('api/likes/<int:pk>/', views.LikeDetail.as_view()),
    path('api/likes/', views.LikeList.as_view()),




    
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    
     
    path('auth2/',include('allauth.urls')),

     path('api/register/', views.RegisterAPI.as_view(), name='auth_register'),


    
    path('',TemplateView.as_view(template_name='help.html')),
]
