from django.contrib import admin
from .models import Category, Figures

# Register your models here.

admin.site.register(Figures)
admin.site.register(Category)