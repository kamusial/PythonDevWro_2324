import random
from typing import Iterable

from django.contrib.auth.models import auth
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.text import slugify
from django.views import View

from .forms import CreateFlashcardForm
from .models import Flashcard, UserFlashcardOwnership


def index(request):
    logout = request.GET.get("logout")
    return render(request, "flashcards/index.html", {"logout": logout})


def learn_flashcard(request, slug):
    flashcard = get_object_or_404(Flashcard, slug=slug)
    user_flashcards = _get_user_flashcards(request)
    user_flashcards.remove(flashcard)
    if user_flashcards:
        next_flashcard: Flashcard = random.choice(user_flashcards)
    else:
        next_flashcard = flashcard
    return render(request,
                  "flashcards/learn-flashcard.html",
                  context={
                      "flashcard": flashcard,
                      "next_flashcard_url": next_flashcard.learn_url()
                  }
                  )


def learn_flashcard_redirect(request):
    random_flashcard: Flashcard = random.choice(_get_user_flashcards(request))
    return redirect(reverse("flashcard-learn", args=[random_flashcard.slug]))


class FlashcardList(View):

    def get(self, request: HttpRequest):
        form = CreateFlashcardForm()
        context = self._create_context(request, form)
        return render(request, "flashcards/flashcard-list.html", context=context)

    def post(self, request: HttpRequest):
        if request.POST.get("requestType") == "DELETE":
            return self.delete(request)
        form = CreateFlashcardForm(request.POST)
        if form.is_valid():
            user = auth.get_user(request)
            new_flashcard = Flashcard(**form.cleaned_data,
                                      slug=slugify(form.cleaned_data["name"]))
            new_flashcard.save()
            new_ownership = UserFlashcardOwnership(user=user, flashcard=new_flashcard)
            new_ownership.save()
            return redirect(reverse("flashcards-collection"))
        context = self._create_context(request, form)
        return render(request, "flashcards/flashcard-list.html", context=context)

    def delete(self, request: HttpRequest):
        slug = request.POST.get("slug")
        Flashcard.objects.filter(slug=slug).delete()
        return redirect(reverse("flashcards-collection"))

    def _create_context(self, request, form):
        flashcards = _get_user_flashcards(request)
        context = {
            "flashcards": flashcards,
            "form": form
        }
        return context


def _get_user_flashcards(request) -> list[Flashcard]:
    user = auth.get_user(request)
    user_ownerships: Iterable[UserFlashcardOwnership] = UserFlashcardOwnership.objects.filter(
        user__username=user.username)
    user_flashcards = [ownership.flashcard for ownership in user_ownerships]
    return user_flashcards


""" 
jako funkcja:
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
    return render(request, "flashcards/flashcard-list.html", context=context)
"""
