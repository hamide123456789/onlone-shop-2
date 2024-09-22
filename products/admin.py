from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Product, Comment


class CommentsInLine(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active', ]
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']

    inlines = [
        CommentsInLine,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active', ]
