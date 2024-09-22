# models.py
from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=100)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='comments', null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
