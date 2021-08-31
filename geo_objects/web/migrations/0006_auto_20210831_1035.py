# Generated by Django 3.2.6 on 2021-08-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20210831_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=64, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, null=True, verbose_name='slug'),
        ),
    ]