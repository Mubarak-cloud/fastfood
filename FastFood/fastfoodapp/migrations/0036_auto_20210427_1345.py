# Generated by Django 3.1.7 on 2021-04-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0035_auto_20210426_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='It_Descrip',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='It_Prise',
            field=models.PositiveIntegerField(default=0.0),
        ),
    ]