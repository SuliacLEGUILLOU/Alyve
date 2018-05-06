from django.contrib import admin

from django.contrib.auth.models import User
from .models import Page, Article, Comment, Category, Blog, Question, Link, Social, Media

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    fieldsets = [
        ('Information', {'fields': ['name']})
    ]

class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'displayed')
    fieldsets = [
        ('Page', {'fields': ['name', 'content', 'displayed', 'cover']})
    ]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    fieldsets = [
        ('Question', {'fields': ['question', 'answer']})
    ]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'hide_image', 'publication_date', 'update_date', 'comments_count', 'unvalided_comments_count')
    fieldsets = [
        ('Article', {'fields': ['title', 'content', 'category', 'published', 'hide_image', 'disclaimer', 'cover', 'author']}),
        ('Date information', {'fields': ['publication_date', 'update_date']}),
    ]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'publication_date', 'content', 'valided')

class SocialAdmin(admin.ModelAdmin):
    list_display = ('network', 'link', 'sidebar')

class MediaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'file', 'title')

class LinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'shortcut', 'sort')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Media, MediaAdmin)