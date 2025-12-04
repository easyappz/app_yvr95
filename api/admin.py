from django.contrib import admin
from .models import Member, Post, Like, Comment


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at')
    search_fields = ('content', 'author__username')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('user', 'post', 'created_at')
    search_fields = ('user__username', 'post__content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'content')
    list_filter = ('user', 'post', 'created_at')
    search_fields = ('user__username', 'post__content', 'content')
