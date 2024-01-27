from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("flashcards/items/<slug:slug>", views.learn_flashcard),
    path("flashcards", views.flashcard_list)
]
