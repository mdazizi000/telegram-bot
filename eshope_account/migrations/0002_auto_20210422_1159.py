# Generated by Django 3.1.4 on 2021-04-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshope_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code_meli',
            field=models.CharField(blank=True, max_length=16, verbose_name='کدملی'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=12, verbose_name='شماره همراه'),
        ),
    ]
