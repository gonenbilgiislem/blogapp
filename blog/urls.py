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
    path("blogs/<slug:slug>", views.blog_details,name="blog_details"),
    path("category/<slug:slug>", views.blogs_by_category,name="blogs_by_category"),
    path("admin/",views.admin ,name="admin")

]
