from django.shortcuts import render, get_object_or_404
from .models import Producto
from categorias.models import Category


# Create your views here.
def store(request, slug=None):
    category = None 
    product = None
     # Verificar si viene categoría por GET o por URL
    category_param = request.GET.get('category')
    
    if slug != None:
        category = get_object_or_404(Category, slug=slug)
        products = Producto.objects.all().filter(category=category, is_available=True)#variable de productos filtrados por disponibles
        #details = Producto.objects.all().filter()

    elif category_param:#filtrar por categori de param get
        category = get_object_or_404(Category, slug=category_param)
        products= Producto.objects.filter(category=category, is_available=True)

    else:
        products = Producto.objects.all().filter(is_available=True)
        
    # Filtrar por búsqueda (keyword), el nombre que le coloque al input html
    keyword = request.GET.get('keyword')
    if keyword:
        products = products.filter(name__icontains=keyword) | products.filter(#incontains equuivale a like en sql
        category__name_category__icontains=keyword)
    
    counter_products = products.count()
    context = {
        "products" : products,
        "counter_products": counter_products

    }
    return render(request, "store/tienda.html", context=context)

