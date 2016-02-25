from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Name(models.Model):
    name_text = models.CharField(max_length=24)
    reddit = models.CharField(max_length=24, default='Your Reddit uname')
    upvotes = models.IntegerField(default=1)
    picture = models.CharField(max_length=1024, default="https://upload.wikimedia.org/wikipedia/en/7/7e/Patrick_Star.png")
    def __str__(self):
        return self.name_text

class Posts(models.Model):
    title_text = models.CharField(max_length=72)
    author = models.CharField(max_length=16, default='MarlosTiltingMe')
    body_text = models.CharField(max_length=2048)
    img = models.CharField(max_length=1024)
    log_text = models.CharField(max_length=9000, default="No logs available.")
    def __str__(self):
        return self.title_text
