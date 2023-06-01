from django.contrib import admin
from .models import Post, Categorie, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Categorie)
admin.site.register(Comment)
