from django import forms
from django.utils.text import slugify

from .models import Flashcard


class CreateFlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ["name", "question", "answer"]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        slug = slugify(name)
        if Flashcard.objects.filter(slug=slug).exists():
            raise forms.ValidationError("Flashcard with that name already exists")
        return name
