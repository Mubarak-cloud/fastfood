# Generated by Django 3.1.7 on 2021-05-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0002_auto_20210509_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='R_Email',
            field=models.EmailField(default='null', max_length=200, unique=True),
        ),
    ]
