# Generated by Django 4.1.7 on 2023-02-27 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
