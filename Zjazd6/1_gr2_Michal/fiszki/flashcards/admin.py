from django.contrib import admin
from .models import Flashcard


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
