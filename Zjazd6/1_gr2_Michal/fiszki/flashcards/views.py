from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.text import slugify

from .models import Flashcard
from .forms import CreateFlashcardForm


def index(request):
    return render(request, "index.html")


def learn_flashcard(request, slug):
    flashcard = get_object_or_404(Flashcard, slug=slug)
    return render(request, "learn-flashcard.html", context={"flashcard": flashcard})


def flashcard_list(request: HttpRequest):
    form = CreateFlashcardForm()
    if request.method == "POST":
        form = CreateFlashcardForm(request.POST)
        if form.is_valid():
            new_flashcard = Flashcard(**form.cleaned_data,
                                      slug=slugify(form.cleaned_data["name"]))
            new_flashcard.save()
            return redirect(reverse("flashcards-collection"))
    flashcards = Flashcard.objects.all()
    context = {
        "flashcards": flashcards,
        "form": form
    }
    return render(request, "flashcard-list.html", context=context)
