# Generated by Django 4.1.5 on 2023-02-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaApp', '0007_alter_details_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='date',
            field=models.CharField(max_length=4),
        ),
    ]
