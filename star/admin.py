from django.contrib import admin

from .models import Blog_post, Comment

admin.site.register(Blog_post)
admin.site.register(Comment)