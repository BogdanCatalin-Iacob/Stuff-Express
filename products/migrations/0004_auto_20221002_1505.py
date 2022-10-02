# Generated by Django 3.2.15 on 2022-10-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220927_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='market_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]