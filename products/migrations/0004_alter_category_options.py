# Generated by Django 4.0.5 on 2022-07-03 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_product_owner_alter_product_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categorys'},
        ),
    ]
