from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("flashcards/learn", views.learn_flashcard_redirect, name="learn"),
    path("flashcards/items/<slug:slug>", views.learn_flashcard, name="flashcard-learn"),
    path("flashcards",
         login_required(views.FlashcardList.as_view(), login_url="user-login"),
         name="flashcards-collection")
]
