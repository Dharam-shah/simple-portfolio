from django.contrib import admin
from .models import Homepage, Blog

# Register your models here.

# admin.site.register(Homepage)
# admin.site.register(Blog)

class HomepageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(Homepage, HomepageAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at']

admin.site.register(Blog, BlogAdmin)
