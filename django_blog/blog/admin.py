from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'published_date')
    list_filter=('author', 'published_date')
    search_fields=('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('post', 'author', 'created_at')
    search_fields=('author_username', 'content')