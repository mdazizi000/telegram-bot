# Generated by Django 3.1.4 on 2021-04-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshope_products', '0005_products_subcategories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discription',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
    ]
