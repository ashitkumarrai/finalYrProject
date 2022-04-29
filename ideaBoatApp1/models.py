from django.db import models
from requests import post



def increment_post_category_number():
    last_id = Post_Category.objects.all().order_by('created').last()

    if not last_id:
        return 'idb-category-' + '0001'

    post_id = last_id.id
    post_int = post_id[13:]
    new_post_int = int(post_int) + 1
    new_post_id = 'idb-category-'+ str(new_post_int).zfill(4)

    return new_post_id   

class Post_Category(models.Model):
    name=models.CharField(max_length=100, blank=False, default='WEB APPLICATION')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)
    id = models.CharField(max_length=17, default=increment_post_category_number, editable=False,primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


def increment_post_id_number():
    last_id = Post.objects.all().order_by('posted_on').last()

    if not last_id:
        return 'idb-post-' + '0001'

    post_id = last_id.id
    post_int = post_id[9:]
    new_post_int = int(post_int) + 1
    new_post_id = 'idb-post-'+ str(new_post_int).zfill(4)

    return new_post_id

def increment_likes_id_number():
    last_id = PostLikes.objects.all().order_by('created').last()

    if not last_id:
        return 'idb-likes-' + '0001'

    likes_id = last_id.id
    post_int = likes_id[10:]
    new_post_int = int(post_int) + 1
    new_post_id = 'idb-likes-'+ str(new_post_int).zfill(4)

    return new_post_id

def increment_comment_id_number():
    last_id = Comment.objects.all().order_by('created').last()

    if not last_id:
        return 'idb-comment-'+ '0001'

    post_id = last_id.id
    post_int = post_id[12:]
    new_post_int = int(post_int) + 1
    new_post_id = 'idb-comment-'+ str(new_post_int).zfill(4)

    return new_post_id






class Post(models.Model):
    title=models.CharField(max_length=100)
    slug = models.SlugField(max_length=255,unique=True, null=True, blank=True)
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    owner= models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='posts')    
    publish=models.BooleanField(default=False)

    id = models.CharField(max_length=17, default=increment_post_id_number, editable=False,primary_key=True)
    
    

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
    id = models.CharField(max_length=17, default=increment_likes_id_number, editable=False,primary_key=True)


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
    id = models.CharField(max_length=17, default=increment_comment_id_number, editable=False,primary_key=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-created']



