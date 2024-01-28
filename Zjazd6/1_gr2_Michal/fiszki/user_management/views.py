from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("flashcards-collection")

    context = {
        "form": form,
        "form_title": "Please Register"
    }
    return render(request,
                  "user_management/user-form.html",
                  context=context)


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("flashcards-collection")
    context = {
        "form": form,
        "form_title": "Please provide your credentials"
    }
    return render(request,
                  "user_management/user-form.html",
                  context=context)


def user_session(request):
    """ context_processor """
    user = auth.get_user(request)
    return {"user": user}
