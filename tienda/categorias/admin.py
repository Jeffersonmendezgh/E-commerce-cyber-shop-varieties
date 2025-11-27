from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista del admin
    list_display = ('name_category', 'slug', 'description')
    
    # Permite buscar por estos campos
    search_fields = ('name_category', 'description')
    
    # Filtros laterales (útil si tienes muchas categorías)
    list_filter = ('name_category',)
    
    # Campos que se autocompletan al escribir (slug se genera desde nombre_categoria)
    prepopulated_fields = {'slug': ('name_category',)}
        
    # Número de elementos por página en la lista
    list_per_page = 20

    # Método personalizado para mostrar una versión corta de la descripción
    def descripcion_corta(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    descripcion_corta.short_description = 'description'  # Nombre de la columna en el admin