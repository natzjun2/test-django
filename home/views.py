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
    users = [
        {"id": 1, "name": "Briones", "email": "briones@gmail.com"},
        {"id": 2, "name": "Blando", "email": "blando@gmail.com"},
        {"id": 3, "name": "Bradi", "email": "bradi@gmail.com"},
    ]

    return render(request, "users.html",
                  {"users": users}
                  )


def products(request):
    pro = [
        {"id": 1, "name": "Laptop", "price": "100000"},
        {"id": 2, "name": "Mouse", "price": "500"},
        {"id": 3, "name": "Keyboard", "price": "1000"},
    ]
    prod = { "products" : pro}

    return render(request, "products.html", prod)

