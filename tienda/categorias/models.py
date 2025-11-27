from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name_category = models.CharField(max_length=50, unique=True)
    slug = models.TextField(max_length=100, unique=True)
    description = models.TextField(max_length=225, blank=True)
    image_categoria = models.ImageField(upload_to='fotos/categories', blank=True)

    def get_url(self):
        return reverse("store:products-category",args=[self.slug])
    

    def __str__(self):
        return self.name_category
    
