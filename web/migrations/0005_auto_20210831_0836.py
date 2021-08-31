# Generated by Django 3.2.6 on 2021-08-31 06:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_tag_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Souffle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('elevation', models.PositiveBigIntegerField(verbose_name='Elevation')),
                ('altitude', models.PositiveBigIntegerField(verbose_name='Altitude')),
                ('width', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Width')),
                ('height', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Height')),
                ('lon', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)], verbose_name='Longitude')),
                ('lat', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)], verbose_name='Latitude')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category')),
                ('tags', models.ManyToManyField(blank=True, to='web.Tag')),
            ],
            options={
                'verbose_name_plural': 'Souffle',
                'db_table': 'Suffle',
                'ordering': ('created_time',),
            },
        ),
        migrations.CreateModel(
            name='Sphere',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('elevation', models.PositiveBigIntegerField(verbose_name='Elevation')),
                ('altitude', models.PositiveBigIntegerField(verbose_name='Altitude')),
                ('object_type', models.SmallIntegerField(verbose_name='Object type')),
                ('radius', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Radius')),
                ('lon', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)], verbose_name='Longitude')),
                ('lat', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)], verbose_name='Latitude')),
                ('has_audio', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category')),
                ('tags', models.ManyToManyField(blank=True, to='web.Tag')),
            ],
            options={
                'verbose_name_plural': 'Sphere',
                'db_table': 'Sphere',
                'ordering': ('created_time',),
            },
        ),
        migrations.DeleteModel(
            name='Figures',
        ),
    ]