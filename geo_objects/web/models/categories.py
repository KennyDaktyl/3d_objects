from django.db import models
from .base import BaseModel

class Category (BaseModel):
    name = models.CharField(verbose_name="Category", max_length=64)

    class Meta:
        ordering = (
            "name",
        )
        verbose_name_plural = "Category"
        db_table = "Category"
    
    def __str__(self):
        return self.name