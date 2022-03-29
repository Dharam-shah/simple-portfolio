from django.urls import path
from .views import index, contact, blog, blog_detail, blog_create, blog_update, blog_delete

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("blog/", blog, name="blog"),
    path("blog_detail/<int:id>", blog_detail, name="blog_detail"),
    path('blog_create/', blog_create, name="blog_create"),
    path('blog_update/<int:id>', blog_update, name="blog_update"),
    path('blog_delete/<int:id>', blog_delete, name="blog_delete")
]