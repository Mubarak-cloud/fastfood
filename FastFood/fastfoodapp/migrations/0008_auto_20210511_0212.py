# Generated by Django 3.1.7 on 2021-05-11 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0007_remove_restaurant_r_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='R_Image',
            field=models.ImageField(default='null', upload_to='media/media/media/media'),
        ),
    ]
