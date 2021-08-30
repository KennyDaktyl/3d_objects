from .base import BaseModel
from django.db import models

from django.template.defaultfilters import slugify


class Tag(BaseModel):
    name = models.CharField(max_length=64)
    slug  = models.SlugField(max_length=128, blank=True, null=True)

    class Meta:
        ordering = (
            "created_time",
        )
        verbose_name_plural = "Tags"
        db_table = "tags"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name