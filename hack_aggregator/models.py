from django.db import models
import uuid

class Author(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    followers = models.IntegerField()
    avatar = models.URLField(max_length=200)
    profile_text = models.TextField()

    def __str__(self):
        return self.name

class Content(models.Model):
    author = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True, editable=False)
    created_at = models.DateTimeField()
    main_text = models.TextField()
    origin_url = models.URLField(max_length=200)
    media = models.JSONField(blank=True, null=True)  # Storing URLs in a JSON field
    likes = models.IntegerField()
    views = models.IntegerField()
    comments = models.IntegerField()

    def __str__(self):
        return f'{self.author.name}: {self.main_text[:50]}'
