from django.shortcuts import render, redirect
from django.http import HttpResponse
from pages.models import Blog, Homepage
from .forms import BlogForm, BlogModelForm

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
    'image':homepage_data.image,
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

# create new blog
def blog_create(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST,request.FILES)
        if form.is_valid():
            Blog.objects.create(**form.cleaned_data)
            #form.save()
            return redirect('/blog')
        else:
             print('form is not valid')
             print(form.errors)
             return HttpResponse('error')
    else:
        form = BlogModelForm()

    return render(request, 'blogs/blog_create.html', {'form': form})

# update blog
def blog_update(request,id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = BlogModelForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            #Blog.objects.filter(id=id).update(**form.cleaned_data)
            form.save()
            #return redirect('/blog')
            return redirect('/blog_detail/'+str(form.instance.id))
        else:
            print('form is not valid')
            print(form.errors)
            return HttpResponse('error')
    else:
        form = BlogModelForm(instance=blog)
    return render(request, 'blogs/blog_update.html', {'form': form})

#delete blog
def blog_delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('/blog')