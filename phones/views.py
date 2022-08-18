from django.shortcuts import render, redirect
from phones.models import Phones

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sortirovka = request.GET.get("sort")
    if sortirovka == "min_price":
        sortirovka = "price"
    elif sortirovka == "max_price":
        sortirovka = "-price"
    context = {
        'phones': Phones.objects.all().order_by(sortirovka)
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phones.objects.filter(slug=slug)
    print("Ok", list(phones)[0])
    context = {
        'phone': list(phones)[0]
    }
    return render(request, template, context)