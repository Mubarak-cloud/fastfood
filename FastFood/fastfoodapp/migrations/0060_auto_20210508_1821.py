# Generated by Django 3.1.7 on 2021-05-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0059_auto_20210508_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='D_Name',
            field=models.CharField(default='null', max_length=200),
        ),
    ]