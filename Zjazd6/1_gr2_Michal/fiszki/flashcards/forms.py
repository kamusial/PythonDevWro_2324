from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.utils.text import slugify

from .models import Flashcard


class CreateFlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ["name", "question", "answer"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "hiddenForm"
        self.helper.add_input(
            Submit("submit",
                   "Create New Flashcard")
        )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        slug = slugify(name)
        if Flashcard.objects.filter(slug=slug).exists():
            raise forms.ValidationError("Flashcard with that name already exists")
        return name
