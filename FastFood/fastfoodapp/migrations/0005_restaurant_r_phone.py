# Generated by Django 3.0.5 on 2021-04-23 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0004_auto_20210423_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='R_Phone',
            field=models.IntegerField(default=0),
        ),
    ]