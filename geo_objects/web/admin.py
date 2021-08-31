from django.contrib import admin
from .models import Category, Sphere, Souffle, Tag

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]
    search_fields = ('name', )
    exclude = ['id']

@admin.register(Sphere)
class SphereAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Sphere._meta.fields]
    list_filter = (
        'category__name',
        'object_type',
        'has_audio',
        'tags',
        
    )
    search_fields = ('name', )
    exclude = ['id']
    ordering = ['name']

@admin.register(Souffle)
class SouffleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Souffle._meta.fields]
    list_filter = (
        'category__name',
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
