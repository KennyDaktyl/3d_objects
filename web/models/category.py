from django.db import models
from .base import BaseModel

from django.template.defaultfilters import slugify

class Category (BaseModel):
    name = models.CharField(verbose_name="Category", max_length=64)
    slug  = models.SlugField(verbose_name="slug", max_length=128, blank=True, null=True)

    class Meta:
        ordering = (
            "name",
        )
        verbose_name_plural = "Category"
        db_table = "Category"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name