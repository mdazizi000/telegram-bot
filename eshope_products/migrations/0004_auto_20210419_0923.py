# Generated by Django 3.1.4 on 2021-04-19 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshope_products', '0003_products_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discription',
            field=models.TextField(null=True, verbose_name='توضیحات'),
        ),
    ]