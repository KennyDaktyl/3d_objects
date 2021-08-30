from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .base import BaseModel
from .categories import Category
from .tags import Tag

class Figures (BaseModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    name = models.CharField(verbose_name="Name", max_length=64)
    elevation = models.PositiveBigIntegerField(verbose_name="Elevation")
    altitude = models.PositiveBigIntegerField(verbose_name="Altitude")
    object_type = models.SmallIntegerField(verbose_name="Object type")
    lon = models.FloatField(verbose_name="Longitude", 
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])
    lat = models.FloatField(verbose_name="Latitude",
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
    )
    tags = models.ManyToManyField('Tag', blank=True)

    class Meta:
        ordering = (
            "created_time",
        )
        verbose_name_plural = "Figures"
        db_table = "Figures"
    
    def __str__(self):
        return self.name