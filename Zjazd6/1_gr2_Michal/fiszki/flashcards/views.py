from django.shortcuts import render, get_object_or_404
from .models import Flashcard
from .forms import CreateFlashcardForm


def index(request):
    return render(request, "index.html")


def learn_flashcard(request, slug):
    flashcard = get_object_or_404(Flashcard, slug=slug)
    return render(request, "learn-flashcard.html", context={"flashcard": flashcard})


def flashcard_list(request):
    form = CreateFlashcardForm()
    flashcards = Flashcard.objects.all()
    context = {
        "flashcards": flashcards,
        "form": form
    }
    return render(request, "flashcard-list.html", context=context)
