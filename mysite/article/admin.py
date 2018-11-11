from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'content', 'created_time')

admin.site.register(Article, ArticleAdmin)
