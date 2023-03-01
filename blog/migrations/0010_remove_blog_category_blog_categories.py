# Generated by Django 4.1.7 on 2023-03-01 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(related_name='blogs', to='blog.category'),
        ),
    ]
