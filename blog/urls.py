from django.urls import path
from blog import views
urlpatterns = [
    path("hadicanımsende", views.index,name="index"),
    path('', views.index,name="home"),
    path("index", views.index,name="index"),
    path("blogs", views.blogs,name="blogs"),
    path("blog", views.blogs,name="blogs"),
    path("blog/", views.blogs,name="blogs"),
    path("blogs/", views.blogs,name="blogs"),
    path("blogs/<int:id>", views.blog_details,name="blog_details"),
    path("admin",views.admin ,name="admin")

]
