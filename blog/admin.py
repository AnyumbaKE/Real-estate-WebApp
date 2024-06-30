from django.contrib import admin
from .models import Post, categories, PostComment

admin.site.register(Post)
admin.site.register(PostComment)