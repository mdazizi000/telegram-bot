# Generated by Django 3.1.4 on 2021-04-19 07:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eshope_products', '0008_remove_products_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
