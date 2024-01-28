from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import auth
from django.urls import reverse
from django.utils.text import slugify
from django.views import View
from django.db.models import Q
import random
from .models import Flashcard, UserFlashcardOwnership
from .forms import CreateFlashcardForm


def index(request):
    return render(request, "flashcards/index.html")


def learn_flashcard(request, slug):
    flashcard = get_object_or_404(Flashcard, slug=slug)
    random_flashcard: Flashcard = random.choice(Flashcard.objects.filter(~Q(slug=flashcard.slug)))
    return render(request,
                  "flashcards/learn-flashcard.html",
                  context={
                      "flashcard": flashcard,
                      "next_flashcard_url": random_flashcard.learn_url()
                  }
                  )


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
        user = auth.get_user(request)
        user_ownerships: list[UserFlashcardOwnership] = UserFlashcardOwnership.objects.filter(user__username=user.username)
        flashcards = [ownership.flashcard for ownership in user_ownerships]
        context = {
            "flashcards": flashcards,
            "form": form
        }
        return context


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