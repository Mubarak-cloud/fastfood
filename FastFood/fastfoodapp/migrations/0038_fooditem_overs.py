# Generated by Django 3.1.7 on 2021-04-27 13:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0037_restaurant_r_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='overs',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
