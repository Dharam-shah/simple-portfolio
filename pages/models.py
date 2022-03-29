from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Homepage(models.Model):
    title = models.CharField(max_length=200)
    para1 = models.TextField()
    para2 = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/Profile-Photo.png')
    skills_list = models.TextField()
    software_list = models.TextField()
    mail = models.EmailField()

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/html.png')
    #btntext = models.CharField(max_length=200)
    paragraph = models.TextField()

    def __str__(self):
        return self.title

