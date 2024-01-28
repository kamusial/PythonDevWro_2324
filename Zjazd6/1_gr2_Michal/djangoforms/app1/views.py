from django.core.handlers.wsgi import HttpRequest
from django.shortcuts import render

from .forms import NameForm


def form1(request: HttpRequest):
    context = {}
    if request.method == "POST":
        name = request.POST.get("imie")
        surname = request.POST.get("nazwisko")
        context["imie_z_formularza"] = name
        context["nazwisko_z_formularza"] = surname
    return render(request,
                  "form1.html",
                  context=context)


def form2(request: HttpRequest):
    context = {
        "form": NameForm()
    }
    if request.method == "POST":
        form = NameForm(request.POST)
        context["form"] = form
        if form.is_valid():
            name = form.cleaned_data.get("imie")
            surname = request.POST.get("nazwisko")
            context["imie_z_formularza"] = name
            context["nazwisko_z_formularza"] = surname
    return render(request,
                  "form2.html",
                  context=context)


def form3(request):
    context = {
        "form": NameForm()
    }
    if request.method == "POST":
        form = NameForm(request.POST)
        context["form"] = form
        if form.is_valid():
            name = form.cleaned_data.get("imie")
            surname = request.POST.get("nazwisko")
            context["imie_z_formularza"] = name
            context["nazwisko_z_formularza"] = surname
    return render(request,
                  "form3.html",
                  context=context)
