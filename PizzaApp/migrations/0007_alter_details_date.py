# Generated by Django 4.1.5 on 2023-02-21 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaApp', '0006_alter_details_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='date',
            field=models.DateField(),
        ),
    ]
