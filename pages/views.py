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
    blog_list = [
        {
            'id':1,
            'title':'HTML',
            'subtitle':'The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.',
            'date':'15 Feb 2022',
            'image':'img/html.png',
            'btntext':'Read more about this blog &#8599;',
            'paragraph':'HTML (HyperText Markup Language) is the most basic building block of the Web. It defines the meaning and structure of web content. Other technologies besides HTML are generally used to describe a web pages appearance/presentatio (CSS) or functionality/behavior (JavaScript). <br> <br> Hypertext refers to links that connect web pages to one another, either within a single website or between websites. Links are a fundamental aspect of the Web. By uploading content to the Internet and linking it to pages created by other people, you become an active participant in the World Wide Web.'
        },
        {
            'id':2,
            'title':'CSS',
            'subtitle':'Cascading Style Sheets, or CSS, is a style sheet language used for describing the presentation of a document written in a markup language like HTML.',
            'date':'15 Feb 2022',
            'image':'img/css.jpg',
            'btntext':'Read more about this blog &#8599;',
            'paragraph':'Cascading Style Sheets, or CSS, is a style sheet language used for describing the presentation of a document written in a markup language like HTML. <br> <br> Cascading Style Sheets, or CSS, is a style sheet language used for describing the presentation of a document written in a markup language like HTML.'
        },
        {
            'id':3,
            'title':'Python',
            'subtitle':'Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.',
            'date':'15 Feb 2022',
            'image':'img/python-django.jpg',
            'btntext':'Read more about this blog &#8599;',
            'paragraph':'Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. <br> <br> Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.'
        }
    ]

    for blog in blog_list:
        if blog['id'] == int(id):
            context = {
                'blog':blog,
            }

    return render(request, "blogs/blog_detail.html", context)


