# Generated by Django 4.1.5 on 2023-02-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaApp', '0009_alter_details_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
