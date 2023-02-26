from django.shortcuts import render

data ={
    "blogs": [
        {
            "id": 1,
            "title": "Komple Web Geliştirme",
            "image": "1.jpg",
            "is_active": True,
            "is_home": False,
            "description": "çok iyi bir kurs"
        },
        {
            "id": 2,
            "title": "Python Kursu",
            "image": "2.jpg",
            "is_active": True,
            "is_home": True,
            "description": "çok iyi bir kurs"
        },
        {
            "id": 3,
            "title": "Django Kursu",
            "image": "3.jpg",
            "is_active": False,
            "is_home": True,
            "description": "çok iyi bir kurs"
        },
        {
            "id": 4,
            "title": "Javascripth Kursu",
            "image": "4.jpg",
            "is_active": False,
            "is_home": False,
            "description": "çok iyi bir kurs"
        }
    ]
}

def index(request):
    context = {
        "blogs": data["blogs"],
        "title": "Anasayfa"
    }
    return render(request, 'blog/index.html', context)

def admin(request):
    return render(request, 'admin/index.html')

def blogs(request):
    context = {
        "blogs": data["blogs"],
        "title": "Blog Sayfası"
    }
    return render(request, 'blog/blogs.html', context)

def blog_details(request, id):
    # blogs = data["blogs"]
    # selectedBlog = None
    #
    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog
    blogs = data["blogs"]
    selectedBlog = [blog for blog in blogs if blog["id"] == id][0]
    return render(request, 'blog/blog_details.html', {"blog": selectedBlog})
