from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        "posts": Post.objects.all()  # Query from database that will get all the objects
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
