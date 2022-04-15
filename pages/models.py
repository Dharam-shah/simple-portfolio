from django.db import models

# Create your models here.

""" Homepage Banner Model """
class Homepage_banner(models.Model):
    Banner_title = models.CharField(max_length=200)
    Banner_subtitle = models.CharField(max_length=200)
    Banner_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Banner_title

""" Homepage Blogs,Article page Blog and Blog detail page blog Model """
class Blog(models.Model):
    #blog_image = models.ImageField(upload_to='images/')
    blog_title = models.CharField(max_length=250)
    blog_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f'ID{self.id} | {self.blog_title}'

