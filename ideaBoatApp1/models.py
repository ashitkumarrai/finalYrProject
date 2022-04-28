from django.db import models





class Post_Category(models.Model):
    name=models.CharField(max_length=100, blank=False, default='WEB APPLICATION')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name





class Post(models.Model):
    title=models.CharField(max_length=100)
    slug = models.SlugField(max_length=255,unique=True, null=True, blank=True)
    keyword=models.CharField(max_length=300,null=True)
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    owner= models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='posts')    
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
    post = models.ForeignKey('Post', related_name='likes', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='likes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.BooleanField(default=False)


    def __bool__(self):
        return self.likes
    class Meta:
        ordering = ['-created']

        verbose_name_plural = 'likes'

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-created']



