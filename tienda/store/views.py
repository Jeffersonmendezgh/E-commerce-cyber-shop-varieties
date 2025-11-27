from django.shortcuts import render, get_object_or_404
from .models import Producto
from categorias.models import Category


# Create your views here.
def store(request, category_slug=None):
    category = None 
    product = None
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Producto.objects.all().filter(is_available=True)#variable de productos filtrados por disponibles
        #details = Producto.objects.all().filter()
        counter_products = products.count() #todos los productos

    else:
        products = Producto.objects.all().filter(is_available=True)
        counter_products = products.count()
    context = {
        "products" : products,
        "counter_products": counter_products

    }
    return render(request, "store/tienda.html", context=context)

