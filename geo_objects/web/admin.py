from django.contrib import admin
from .models import Category, Figures, Tag

# Register your models here.

admin.site.register(Figures)
admin.site.register(Category)
admin.site.register(Tag)