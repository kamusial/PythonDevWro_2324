from django.core.handlers.wsgi import HttpRequest
from django.shortcuts import render


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
