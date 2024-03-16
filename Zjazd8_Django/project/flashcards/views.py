from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Flashcard
from random import choice


def index(request):
    flashcards = Flashcard.objects.all()
    return render(request, "index.html", context={"flashcards": flashcards})


def learn_flashcard(request, flashcard_slug):
    flashcard = Flashcard.objects.get(slug=flashcard_slug)
    return render(request, "learn-flashcard.html", context={"flashcard": flashcard})


def learn(request):
    flashcards = Flashcard.objects.all()
    random_flashcard: Flashcard = choice(flashcards)
    return redirect(f"/flashcards/learn/{random_flashcard.slug}")
