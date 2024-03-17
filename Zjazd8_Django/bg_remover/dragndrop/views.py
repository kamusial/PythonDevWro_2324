from django.http import HttpRequest
from django.shortcuts import render
from .forms import ImageForm
from PIL import Image
import rembg
import io
import base64


def index(request: HttpRequest):
    form = ImageForm()
    context = {"form": form}
    if request.method == "POST":
        image_stream = request.FILES["img"]
        image_input = Image.open(image_stream)
        image_output = rembg.remove(image_input)
        io_stream = io.BytesIO()
        image_output.save(io_stream, "PNG")
        encoded_img_data = base64.b64encode(io_stream.getvalue())
        context["img_no_bg"] = encoded_img_data.decode()
        return render(request, "index.html", context=context)
    return render(request, "index.html", context=context)
