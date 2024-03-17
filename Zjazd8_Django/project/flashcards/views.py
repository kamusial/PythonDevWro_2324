from random import choice

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.text import slugify

from .forms import NewFlashcardForm
from .models import Flashcard, UserFlashcardRelationship


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


@login_required(login_url="login")
def learn(request):
    flashcards = Flashcard.objects.all()
    random_flashcard: Flashcard = choice(flashcards)
    return redirect(random_flashcard.learn_url())


@login_required(login_url="login")
def flashcards_list(request):
    if request.method == "POST":
        flashcard_slug = request.POST["flashcard_slug"]
        flashcard = Flashcard.objects.filter(slug=flashcard_slug)
        if flashcard.exists():
            flashcard.delete()
        return redirect("flashcards-list")
    user_relationships = UserFlashcardRelationship.objects.filter(user__username=request.user.username)
    flashcards: list[Flashcard] = [relationship.flashcard for relationship in user_relationships]
    return render(request, "flashcard-list.html", context={"flashcards": flashcards})


@login_required(login_url="login")
def add_flashcard(request):
    form = NewFlashcardForm()
    if request.method == "POST":
        form = NewFlashcardForm(request.POST)
        flashcard = form.save()
        new_relationship = UserFlashcardRelationship(user=request.user, flashcard=flashcard)
        new_relationship.save()
        return redirect("flashcards-list")
    return render(request, "add-flashcard.html", context={"form": form})
