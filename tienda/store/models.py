from django.db import models
from categorias.models import Category
# Create your models here.

class Producto(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=400, unique=True, blank=True)
    cost = models.IntegerField()
    image = models.ImageField(upload_to="img/products/")#se crea automaticamente
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )
    date_creation = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name