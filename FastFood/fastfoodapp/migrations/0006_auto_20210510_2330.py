# Generated by Django 3.1.7 on 2021-05-10 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0005_auto_20210510_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='F_Images',
            field=models.ImageField(default='null', upload_to='media/media/media'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='R_Image',
            field=models.ImageField(default='null', upload_to='media/media/media'),
        ),
    ]