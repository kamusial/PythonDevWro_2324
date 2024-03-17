from typing import Optional

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import CreateUserForm, LoginForm


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        form.save()
        return redirect("login")
    return render(request, "user_form.html", context={"form": form})


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        #  Optional[User]    ====   User | None
        user: Optional[User] = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("flashcards-list")
    return render(request, "user_form.html", context={"form": form})
