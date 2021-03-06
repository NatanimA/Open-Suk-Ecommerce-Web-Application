# Generated by Django 4.0.5 on 2022-07-04 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='trending',
            field=models.BooleanField(default=False, help_text='0=default,1=trending'),
        ),
    ]
