from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("flashcards/items/<slug:slug>", views.learn_flashcard, name="flashcard-learn"),
    path("flashcards", views.FlashcardList.as_view(), name="flashcards-collection")
]
