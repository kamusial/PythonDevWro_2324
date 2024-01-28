from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
import re


class NameForm(forms.Form):
    imie = forms.CharField(max_length=10)
    nazwisko = forms.CharField(max_length=10)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit("submit",
                   "WYŚLIJ")
        )

    def clean_imie(self):
        imie: str = self.cleaned_data.get("imie")
        imie = imie.capitalize()
        if re.search(r"\W", imie) is not None:
            raise forms.ValidationError("Imię powinno składać się tylko z liter!")
        return imie
