from django.shortcuts import render


def index(request):
    context = {
        "Band": "1975",
        "Genre": "pop",
        "Songs": ["Chocolate", "Menswear", "Love it if we made it"]
    }
    return render(request, "index.html", context)
