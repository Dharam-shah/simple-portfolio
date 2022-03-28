from django.shortcuts import render
from django.http import HttpResponse

from pages.models import Blog, Homepage

# Create your views here.

def index(request):
    #homepage_data = Homepage.objects.all()
    homepage_data = Homepage.objects.get(id=1)
    context = {
    'title':homepage_data.title,
    'para1':homepage_data.para1,
    'para2':homepage_data.para2,
    'skills':homepage_data.skills_list,
    'software':homepage_data.software_list,
    'mail':homepage_data.mail,
    }
    return render(request, "pages/index.html", context)

def contact(request):
    return render(request, "pages/contact.html")

def blog(request):
    blog_list = Blog.objects.all()
    
    context = {
        'blog_lists': blog_list,
    }
    return render(request, "blogs/blog.html", context)

def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog' : blog
    }
    
    return render(request, "blogs/blog_detail.html", context)


