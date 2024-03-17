from django.contrib import admin
from .models import Flashcard, UserFlashcardRelationship


admin.site.register(Flashcard)
admin.site.register(UserFlashcardRelationship)
