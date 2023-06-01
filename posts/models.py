from django.db import models
from django.conf import settings

from django.contrib.auth.models import User


# Create your models here.

class Categorie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    categorie = models.ForeignKey(Categorie, blank=True, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    publication_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name="blog_posts")

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.comment)
