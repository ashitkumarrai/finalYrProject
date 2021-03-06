# Generated by Django 4.0.4 on 2022-04-29 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ideaBoatApp1.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('body', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('publish', models.BooleanField(default=False)),
                ('id', models.CharField(default=ideaBoatApp1.models.increment_post_id_number, editable=False, max_length=17, primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-posted_on',),
            },
        ),
        migrations.CreateModel(
            name='PostLikes',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('likes', models.BooleanField(default=False)),
                ('id', models.CharField(default=ideaBoatApp1.models.increment_likes_id_number, editable=False, max_length=17, primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='ideaBoatApp1.post')),
            ],
            options={
                'verbose_name_plural': 'likes',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post_Category',
            fields=[
                ('name', models.CharField(default='WEB APPLICATION', max_length=100)),
                ('id', models.CharField(default=ideaBoatApp1.models.increment_post_category_number, editable=False, max_length=17, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ManyToManyField(blank=True, related_name='categories', to='ideaBoatApp1.post')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('comment_content', models.TextField()),
                ('id', models.CharField(default=ideaBoatApp1.models.increment_comment_id_number, editable=False, max_length=17, primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ideaBoatApp1.post')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
