from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    if request.method == "POST":
        name = request.POST["first_name"]
        return render(request, "index.html", context={"name": name})
    return render(request, "index.html")
