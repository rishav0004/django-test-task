# Generated by Django 4.0.1 on 2022-03-24 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_product_active_alter_shop_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(null=True, to='ecom.Category'),
        ),
    ]
