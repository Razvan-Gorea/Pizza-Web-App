# Generated by Django 4.1.5 on 2023-02-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaApp', '0013_alter_details_pizza_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, null=True, to='PizzaApp.toppings'),
        ),
    ]