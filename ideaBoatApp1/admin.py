from django.contrib import admin


from .models import Post,Post_Category,Comment

admin.site.register([Post,Post_Category,Comment])
