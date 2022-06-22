from django.contrib import admin
from .models import Post, Comment, Category, Likes

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Likes)