# Generated by Django 3.2.8 on 2021-10-21 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_auto_20211021_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizzaapp',
            options={},
        ),
        migrations.RemoveField(
            model_name='pizzaapp',
            name='created_date',
        ),
    ]
