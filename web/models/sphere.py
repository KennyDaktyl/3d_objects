from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.template.defaultfilters import slugify

from .base import BaseModel
from .category import Category
from .tag import Tag

class Sphere (BaseModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(verbose_name="Name", max_length=64)
    elevation = models.PositiveBigIntegerField(verbose_name="Elevation")
    altitude = models.PositiveBigIntegerField(verbose_name="Altitude")
    object_type = models.SmallIntegerField(verbose_name="Object type", blank=True, null=True)
    radius = models.FloatField(verbose_name="Radius", validators=[MinValueValidator(0.0)])
    lon = models.FloatField(verbose_name="Longitude", 
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])
    lat = models.FloatField(verbose_name="Latitude",
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
    )
    has_audio = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', blank=True)

    slug  = models.SlugField(verbose_name="slug", max_length=128, blank=True, null=True)

    class Meta:
        ordering = (
            "created_time",
        )
        verbose_name_plural = "Sphere"
        db_table = "Sphere"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sphere, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name