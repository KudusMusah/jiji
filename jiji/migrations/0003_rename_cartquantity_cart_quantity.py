# Generated by Django 5.0.3 on 2024-06-07 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jiji', '0002_rename_categoryname_category_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cartQuantity',
            new_name='quantity',
        ),
    ]