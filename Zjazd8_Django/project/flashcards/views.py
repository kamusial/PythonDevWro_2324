from random import choice

from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Flashcard


def index(request):
    flashcards = Flashcard.objects.all()
    return render(request, "index.html", context={"flashcards": flashcards})


def learn_flashcard(request, flashcard_slug):
    flashcard = Flashcard.objects.get(slug=flashcard_slug)
    next_flashcards = Flashcard.objects.filter(pk__gt=flashcard.pk)
    if next_flashcards.exists():
        next_flashcard: Flashcard = next_flashcards.first()
    else:
        next_flashcard: Flashcard = Flashcard.objects.all().first()
    context = {
        "flashcard": flashcard,
        "next_flashcard_url": next_flashcard.learn_url()
    }
    return render(request, "learn-flashcard.html", context=context)


def learn(request):
    flashcards = Flashcard.objects.all()
    random_flashcard: Flashcard = choice(flashcards)
    return redirect(random_flashcard.learn_url())


def flashcards_list(request):
    if request.method == "POST":
        flashcard_slug = request.POST["flashcard_slug"]
        flashcard = Flashcard.objects.filter(slug=flashcard_slug)
        if flashcard.exists():
            flashcard.delete()
        return redirect(reverse("flashcards-list"))
    flashcards = Flashcard.objects.all()
    return render(request, "flashcard-list.html", context={"flashcards": flashcards})
