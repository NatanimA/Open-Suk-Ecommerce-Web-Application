# Generated by Django 4.0.5 on 2022-07-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_brand_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
