# Generated by Django 3.1.7 on 2021-05-14 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0007_auto_20210513_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='foods',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customers',
        ),
        migrations.RemoveField(
            model_name='order',
            name='foods',
        ),
        migrations.RemoveField(
            model_name='order',
            name='restaurants',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='user',
        ),
        migrations.DeleteModel(
            name='Addtocard',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='FoodItem',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
