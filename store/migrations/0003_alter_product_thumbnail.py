# Generated by Django 5.0.5 on 2024-11-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(upload_to='products'),
        ),
    ]
