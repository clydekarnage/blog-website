from django.shortcuts import render


posts = [
    {
        "Author": "Corey MS",
        "Title": "Blog Post 1",
        "Content": "First Post Content",
        "Date_Posted": "August 20, 2018"
    },
    {
        "Author": "Clyde Ibalez",
        "Title": "Blog Post 2",
        "Content": "Second Post Content",
        "Date_Posted": "August 22, 2018"
    }
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
