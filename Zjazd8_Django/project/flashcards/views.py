from django.http import HttpResponse
from django.shortcuts import render
from .models import Flashcard


def index(request):
    flashcards = Flashcard.objects.all()
    return render(request, "index.html", context={"flashcards": flashcards})


def learn(request):
    return render(request, "learn-flashcard.html")