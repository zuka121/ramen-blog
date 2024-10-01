# models.py
from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)
    prefecture = models.CharField(max_length=100, null=True)    
    image = models.ImageField(upload_to='stores/', null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='comments', null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
