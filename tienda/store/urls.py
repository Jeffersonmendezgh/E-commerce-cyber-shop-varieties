#para todas las apps son importantes crear las urls porque no se crea nunca ese archivo
from django.urls import path
from . import views

app_name = "store"

urlpatterns = [#path para la plantilla principal de la tienda
    path('', views.store, name="store"), #le indicamos que nuestra vista se llama store
    path('category/<slug:category_slug>',views.store,name="products-category"),
    #path('category/<slug:category_slug>/<slug:product_sulg>',views.description,name='product_detail'),
]

#python manage.py show_urls