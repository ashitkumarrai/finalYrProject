from django.contrib import admin


from .models import Post,Post_Category,Comment, PostLikes

admin.site.register([Post,Post_Category,Comment,PostLikes])
