# Generated by Django 4.0.4 on 2022-04-26 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideaBoatApp1', '0003_alter_post_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
