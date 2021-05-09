# Generated by Django 3.0.5 on 2021-04-24 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0020_deliveryinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='has',
            name='Delivery_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='fastfoodapp.DeliveryInfo'),
        ),
        migrations.AddField(
            model_name='receive',
            name='Delivery_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='fastfoodapp.DeliveryInfo'),
        ),
    ]