from django.shortcuts import render
from .models import Blog, Category


def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True,is_active=True),
        "categories": Category.objects.all(),
        "title": "Anasayfa"
    }
    return render(request, 'blog/index.html', context)

def admin(request):
    return render(request, 'admin/index.html')

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all(),
        "title": "Blog Sayfası"
    }
    return render(request, 'blog/blogs.html',context)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog/blog_details.html', {"blog": blog})


def blogs_by_category(request,slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.all(),
        # "blogs": Blog.objects.filter(is_active=True,category__blogs=slug),
        "categories": Category.objects.all(),
        "selected_category": slug,
        "title": "Blog Sayfası"
    }
    return render(request, 'blog/blogs.html',context)