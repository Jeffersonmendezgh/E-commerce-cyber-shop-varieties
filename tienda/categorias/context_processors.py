from .models import Category

def menu_links(request):
    links = Category.objects.all()#todas las categorias de db
    return dict(links=links)#devolvemos un dict con la clave links y el valor de todas las categorias que quedan almacenadas en links
