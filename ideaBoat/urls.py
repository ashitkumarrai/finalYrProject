

from pipes import Template
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from ideaBoatApp1.models import Post
from rest_framework import routers, serializers, viewsets
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny, IsAdminUser
from ideaBoatApp1 import views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userss', UserViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
     path('api/posts/', views.PostList.as_view()),
    path('api/posts/<int:pk>/', views.PostDetail.as_view()),

    path('api/comments/', views.CommentList.as_view()),
    path('api/comments/<int:pk>/', views.CommentDetail.as_view()),
    path('api/likes/<int:pk>/', views.LikeListCreate.as_view()),
    
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/',include('allauth.urls')),


    
    path('',TemplateView.as_view(template_name='help.html')),
]