# Generated by Django 3.2.6 on 2021-08-30 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_figures_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, null=True),
        ),
    ]