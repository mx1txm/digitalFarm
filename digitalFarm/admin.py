from django.contrib import admin
from .models import Post, Snippet#, Item,  Category

# Register your models here.
admin.site.register(Post)
#admin.site.register(Category)
#admin.site.register(Item)
admin.site.register(Snippet)