# Generated by Django 3.2.8 on 2021-10-21 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizzaapp',
            old_name='topping',
            new_name='topping1',
        ),
        migrations.AddField(
            model_name='pizzaapp',
            name='topping2',
            field=models.CharField(default=3, max_length=100),
            preserve_default=False,
        ),
    ]
