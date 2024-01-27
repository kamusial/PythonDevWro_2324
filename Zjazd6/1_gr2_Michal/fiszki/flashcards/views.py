from django.shortcuts import render


def index(request):
    return render(request, "flashcard.html", context={"kurs": "4.53"})
