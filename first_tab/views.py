from django.shortcuts import render

# Create your views here.

from .models import FirstTab


def products_list(request):
    products = FirstTab.objects.all()
    context = {
        'products_list': products
    }
    return render(request, "products.html", context)
