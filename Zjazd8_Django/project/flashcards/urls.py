from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('flashcards/', views.flashcards_list, name="flashcards-list"),
    path('flashcards/add/', views.add_flashcard, name="add-flashcard"),
    path('flashcards/learn/', views.learn, name="learn"),
    path('flashcards/learn/<slug:flashcard_slug>', views.learn_flashcard, name="learn-flashcard")
]
