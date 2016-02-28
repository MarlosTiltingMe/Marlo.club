from __future__ import unicode_literals

from django.db import models

class Posts(models.Model):
    title_text = models.CharField(max_length=72, primary_key=True)
    author = models.CharField(max_length=30)
    body_text = models.CharField(max_length=2048)
    img = models.CharField(max_length=1024)
    log_text = models.CharField(max_length=9000, default="No logs available.")
    def __str__(self):
        return self.title_text

class Comments(models.Model):
    parent_thread = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=1024)
    author = models.CharField(max_length=30, default='Anon')
    def __str__(self):
        return self.comment_text

class Members(models.Model):
    member_name = models.CharField(max_length=30, default='Noname')
    img = models.CharField(max_length=1024, default='http://i.imgur.com/y6nAFKz.jpg')
    desc_text = models.CharField(max_length=200, default='No description :(')
    def __str__(self):
        return self.img
