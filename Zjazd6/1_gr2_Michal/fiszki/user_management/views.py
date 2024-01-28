from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CreateUserForm


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("flashcards-collection")

    context = {
        "form": form
    }
    return render(request,
                  "user_management/register.html",
                  context=context)
