# Generated by Django 3.1.7 on 2021-05-10 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0006_auto_20210510_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='R_Email',
        ),
    ]