from django.shortcuts import render
from django.http import request
#impotar el modelo de productos pq queremos mostrarlo aca en el home
from store.models import Producto

#este home de alguba manera se debe conectar con tienda

# Create your views here.
def home(request):
    products = Producto.objects.all().filter(is_available=True) #obtener todos los objetos de tipo producto de db
    context = {
        "products":products
    }
    return render(request, 'home/home.html',context)