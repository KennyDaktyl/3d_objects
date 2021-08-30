from django.contrib import admin
from .models import Category, Figures, Tag

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]
    search_fields = ('name', )
    exclude = ['id']

@admin.register(Figures)
class FiguresAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Figures._meta.fields]
    list_filter = (
        'category__name',
        'object_type',
        'tags',
        
    )
    search_fields = ('name', )
    exclude = ['id']
    ordering = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Tag._meta.fields]
    search_fields = ('name', )
    exclude = ['id']
