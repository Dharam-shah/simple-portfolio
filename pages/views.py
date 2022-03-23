from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "pages/index.html")

def contact(request):
    return render(request, "pages/contact.html")

def blog(request):
    return render(request, "blogs/blog.html")

def blog_detail(request):
    return render(request, "blogs/blog_detail.html")


