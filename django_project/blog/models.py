from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    Date_Posted = models.DateTimeField(default=timezone.now)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  # ---> __str__ is dunder. dunder -> double underscore
        return self.Title
