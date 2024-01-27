from django.db import models
from django.utils.text import slugify


class Flashcard(models.Model):
    name = models.CharField(max_length=200)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
