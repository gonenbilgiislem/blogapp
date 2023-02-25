from django.urls import path
from blog import views
"""
Hadicanımsende url yi değiştirebilirsiniz.
"""
urlpatterns = [
    path('', views.index,name="index"),
    path("index", views.index,name="index"),
    path("blogs", views.blogs,name="blogs"),
    path("blog", views.blogs,name="blogs"),
    path("blog/", views.blogs,name="blogs"),
    path("blogs/", views.blogs,name="blogs"),
    path("blogs/<int:id>", views.blog_details,name="blog_details"),
    path("hadicanımsende", views.index,name="index")
]