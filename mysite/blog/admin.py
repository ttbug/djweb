from django.contrib import admin
from .models import Blog, BlogType
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'blog_type', 'created_time')

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

admin.site.register(Blog, BlogAdmin)

