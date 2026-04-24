from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title" : "Home Page",
        "user" : "Briones",
        "role" : "Programmer",
        "hobbies": ["Bake", "Swimming", "Sleeping"]
    }
    return render(request, "index.html", context)


def users(request):
    return render(request, "users.html")


def products(request):
    return render(request, "products.html")

