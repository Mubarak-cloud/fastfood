# Generated by Django 3.1.7 on 2021-05-13 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0006_auto_20210513_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtocard',
            old_name='fooods',
            new_name='meal',
        ),
        migrations.RemoveField(
            model_name='addtocard',
            name='descrip',
        ),
        migrations.RemoveField(
            model_name='addtocard',
            name='images',
        ),
        migrations.RemoveField(
            model_name='addtocard',
            name='kind',
        ),
        migrations.RemoveField(
            model_name='addtocard',
            name='name',
        ),
        migrations.RemoveField(
            model_name='addtocard',
            name='prise',
        ),
        migrations.RemoveField(
            model_name='addtocard',
            name='size',
        ),
        migrations.AddField(
            model_name='addtocard',
            name='customer_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='fastfoodapp.customer'),
        ),
        migrations.AddField(
            model_name='addtocard',
            name='restaurnt_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='fastfoodapp.restaurant'),
        ),
    ]