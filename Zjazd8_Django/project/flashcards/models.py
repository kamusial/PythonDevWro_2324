from django.db import models


class Flashcard(models.Model):
    name = models.CharField(max_length=100)
    question = models.TextField(max_length=1000)
    answer = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
