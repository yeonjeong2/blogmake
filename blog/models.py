from django.db import models
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank = True, null = True, upload_to = 'blog_photo')

    def __str__(self):
        return self.title

class comment(models.Model):
    comment = models.CharField(max_length = 200)
    data = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete = models.CASCADE)

    def __str__(self):
        return self.comment
