# Generated by Django 3.1.7 on 2021-04-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0030_auto_20210426_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='R_Image',
            field=models.ImageField(default='null', upload_to='media/images'),
        ),
    ]