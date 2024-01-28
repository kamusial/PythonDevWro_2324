from django import forms
from django.forms import TextInput, PasswordInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit("submit",
                   "Create Account",
                   css_class="rounded-pill btn btn-secondary btn-lg w-100 btn-block p-2 mt-4")
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit("submit",
                   "Submit",
                   css_class="rounded-pill btn btn-secondary btn-lg w-100 btn-block p-2 mt-4")
        )