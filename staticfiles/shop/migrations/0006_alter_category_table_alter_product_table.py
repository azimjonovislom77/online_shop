# Generated by Django 5.1.6 on 2025-02-25 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_category'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
