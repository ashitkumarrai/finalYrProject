# Generated by Django 4.0.4 on 2022-04-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideaBoatApp1', '0008_postlikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.AddField(
            model_name='postlikes',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
    ]
