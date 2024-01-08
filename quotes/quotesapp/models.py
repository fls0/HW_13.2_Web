from django.db import models
from taggit.managers import TaggableManager

class Author(models.Model):
    fullname = models.CharField(max_length=255, unique=True)
    born_date = models.CharField(max_length=255, blank=True, null=True)
    born_location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname
    
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.tags

class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f'"{self.quote}" - {self.author.fullname}'
