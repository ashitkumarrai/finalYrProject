from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.


class Post_Category(models.Model):
    CHOICES = (
    ('AI','AI'),
    ('WEB APPLICATION', 'WEB APPLICATION'),
    ('ML','ML'),
    ('EMBEDDED SOFTWARE','EMBEDDED SOFTWARE'),
    ('HARDWARE','HARDWARE'),
)
    
    name=models.CharField(max_length=100,choices=CHOICES, default='WEB APPLICATION')

    def __str__(self):
        return self.name





class Post(models.Model):
    title=models.CharField(max_length=100)
    slug = models.SlugField(max_length=255,unique=True, null=True, blank=True)
    keyword=models.CharField(max_length=300,null=True)
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    owner= models.ForeignKey(User,on_delete=models.CASCADE)    
    post_category = models.ForeignKey(Post_Category,on_delete=models.CASCADE,null=True)
    publish=models.BooleanField()

    class Meta:
        ordering = ('-posted_on',)

    def __str__(self):
        return self.title

    def comment_count(self):
        return Comment.objects.filter(post=self.id).count()


    def like_count(self):
        return PostLikes.objects.filter(post=self.id).count()





class PostLikes(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField(default=False)


    def __str__(self):
        return self.post_id









class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    comment_user = models.ForeignKey(User,on_delete=models.CASCADE)    
    comment_content = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)
    show=models.BooleanField()

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-commented_on']



