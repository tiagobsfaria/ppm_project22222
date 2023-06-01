from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=200)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/profile")

    def __str__(self):
        return self.user.username
