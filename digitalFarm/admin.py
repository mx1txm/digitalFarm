from django.contrib import admin
from .models import Post, Category, Snippet

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Snippet)